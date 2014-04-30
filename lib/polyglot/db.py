from __future__ import division
import json
from collections import defaultdict as dd

class DataBase(object):
    def __init__(self, fp):
        # Use token table for dict compression
        self.tid = 0
        self.tokens = {}
        self.lang_stats = dd(lambda : dd(int))
        self.fp = fp
    
    def next_tid(self):
        self.tid += 1
        return str(self.tid)

    def to_tids(self, tokens):
        tids = []
        for tok in tokens if isinstance(tokens, (list, tuple)) else (tokens,):
            if tok not in self.tokens:
                self.tokens[tok] = self.next_tid()
            tids.append(self.tokens[tok])
        return ','.join(tids)

    def put(self, language, tokens):
        self.lang_stats[language][self.to_tids(tokens)] += 1

    def c_token_on_lang(self, token, lang):
        tid = self.to_tids(token)
        return self.lang_stats.get(lang, {}).get(tid, 0)

    def c_tokens_on_lang(self, lang):
        return sum(self.lang_stats.get(lang, {}).values())

    def c_tokens(self):
        return len(self.tokens)

    def c_token(self, token):
        tid = self.to_tids(token)
        return sum(stats.get(tid, 0) for stats in self.lang_stats.values())

    def languages(self):
        return self.lang_stats.keys()

    def load(self):
        data = json.load(self.fp)
        self.tokens = data['tokens']
        self.lang_stats = data['lang_stats']
        self.tid = len(self.tokens)

    def save(self):
        json.dump(
            # {'tokens': sorted(self.tokens.items(), key=lambda t: int(t[1])),
            {'tokens': self.tokens,
            'lang_stats': self.lang_stats},
            self.fp,
            indent=2,
            sort_keys=False
        )
        self.fp.flush()

if __name__ == '__main__':
    db = DataBase(open('statistics.json'))
    db.load()
    print db.c_tokens_on_lang('Python')
