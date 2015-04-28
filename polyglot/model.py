from __future__ import division
import json
from collections import defaultdict as dd, OrderedDict
from operator import countOf
from functools32 import lru_cache

import logging
logger = logging.getLogger(__name__)

# Since no space is allowed in token, we use it as a separator
TOK_SEP = ' '

class LanguageModel(object):
    def __init__(self, fp):  # Filename should be better?
        # Statistics of tokens in a language,
        # each key is a language name, and the value is a dict
        # consisting of tokens and their occurrence numbers
        # e.g.
        # {
        #     "Python": {
        #         "from": 2,
        #         "os": 1,
        #         "import": 5
        #     },
        #     "Java": {
        #         "import": 5,
        #         "java": 3
        #     }
        # }
        # self.lang_stats = dd(lambda: dd(int))
        self.lang_stats = dd(OrderedDict)
        self.fp = fp
    
    def put(self, language, tokens):
        if tokens not in self.lang_stats[language]:
            self.lang_stats[language][tokens] = 1
        else:
            self.lang_stats[language][tokens] += 1

    @lru_cache(maxsize=None)
    def n_token_on_lang(self, token, lang):
        return self.lang_stats.get(lang, {}).get(token, 0)

    @lru_cache(maxsize=None)
    def n_lang_tokens(self, lang):
        """Returns number of tokens given a specified language"""
        return sum(self.lang_stats.get(lang, {}).values())

    @lru_cache(maxsize=None)
    def n_tokens(self):
        """Returns number of all tokens"""
        return sum(sum(stats.values()) for stats in self.lang_stats.values())

    @lru_cache(maxsize=None)
    def n_token(self, token):
        """Returns number of a specified token"""
        return sum(stats.get(token, 0) for stats in self.lang_stats.values())

    @lru_cache(maxsize=None)
    def languages(self):
        return self.lang_stats.keys()

    def load(self):
        logger.debug('Loading model file...')
        _lang_stats = json.load(self.fp)
        self.lang_stats = dd(dict)
        # Convert a TOK_SEP separated string back to tuple again
        for lang in _lang_stats:
            for token in _lang_stats[lang]:
                self.lang_stats[lang][tuple(token.split(TOK_SEP))] = _lang_stats[lang][token]
        logger.debug('Finished loading')

    def save(self):
        _lang_stats = dd(OrderedDict)
        # Json doesn't allow tuple to be a key, convert it to a TOK_SEP separated string
        for lang in self.lang_stats:
            for token in self.lang_stats[lang]:
                _lang_stats[lang][TOK_SEP.join(token)] = self.lang_stats[lang][token]
        json.dump(
            # {'tokens': sorted(self.tokens.items(), key=lambda t: int(t[1])),
            _lang_stats,
            self.fp,
            indent=2,
            sort_keys=False
        )
        self.fp.flush()

if __name__ == '__main__':
    model = LanguageModel(open('model.json'))
    model.load()
    print model.n_lang_tokens('Python')
