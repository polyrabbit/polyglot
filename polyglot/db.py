from __future__ import division
import json
from collections import defaultdict as dd
from operator import countOf
from functools32 import lru_cache

import logging
logger = logging.getLogger(__name__)

class DataBase(object):
    def __init__(self, fp):  # Filename should be better?
        self.tid = 0
        # Map between token literals and their ids
        # e.g.
        # {
        #     "from": "1",
        #     "urllib2": "2",
        #     "import": "3"
        # }
        self.tokens = {}
        # Statistics of tokens in a language,
        # each key is a language name, and the value is a dict
        # consisting of token ids and their occurrence numbers
        # e.g.
        # {
        #     "Python": {
        #         "1": 2,
        #         "2": 1,
        #         "3": 5
        #     },
        #     "Java": {
        #         "3": 5,
        #         "6": 3
        #     }
        # }
        self.lang_stats = dd(lambda: dd(int))
        self.fp = fp
    
    def next_tid(self):
        self.tid += 1
        return str(self.tid)

    @lru_cache(maxsize=None)
    def to_tids(self, tokens):
        """Replace a token list with the corresponding token ids"""
        tids = []
        for tok in tokens if isinstance(tokens, (list, tuple)) else (tokens,):
            if tok not in self.tokens:
                self.tokens[tok] = self.next_tid()
            tids.append(self.tokens[tok])
        return ','.join(tids)

    def put(self, language, tokens):
        self.lang_stats[language][self.to_tids(tokens)] += 1

    @lru_cache(maxsize=None)
    def c_token_on_lang(self, token, lang):
        tid = self.to_tids(token)
        return self.lang_stats.get(lang, {}).get(tid, 0)

    @lru_cache(maxsize=None)
    def c_tokens_on_lang(self, lang):
        """Returns number of tokens given a specified language"""
        return sum(self.lang_stats.get(lang, {}).values())

    @lru_cache(maxsize=None)
    def c_tokens(self):
        """Returns number of unique tokens"""
        return len(self.tokens)

    @lru_cache(maxsize=None)
    def c_token(self, token):
        """Returns number of a specified token"""
        tid = self.to_tids(token)
        return sum(stats.get(tid, 0) for stats in self.lang_stats.values())

    @lru_cache(maxsize=None)
    def c_once(self):
        return sum(countOf(stats.values(), 1) for stats in self.lang_stats.values())

    @lru_cache(maxsize=None)
    def total_count(self):
        """Returns number of all tokens"""
        return sum(sum(stats.values()) for stats in self.lang_stats.values())

    @lru_cache(maxsize=None)
    def languages(self):
        return self.lang_stats.keys()

    def load(self):
        logger.debug('Loading model file...')
        data = json.load(self.fp)
        logger.debug('Finished loading')
        self.tokens = data['tokens']
        self.lang_stats = data['lang_stats']
        self.tid = len(self.tokens)

    def save(self):
        json.dump(
            # {'tokens': sorted(self.tokens.items(), key=lambda t: int(t[1])),
            {
                'tokens': self.tokens,
                'lang_stats': self.lang_stats
            },
            self.fp,
            indent=2,
            sort_keys=False
        )
        self.fp.flush()

if __name__ == '__main__':
    db = DataBase(open('model.json'))
    db.load()
    print db.c_tokens_on_lang('Python')
    print db.c_once()
