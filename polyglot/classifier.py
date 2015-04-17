#coding: utf-8
from __future__ import division
import os
import collections
import logging

from .db import DataBase
from .tokenizer import tokenize, Ngrams

logger = logging.getLogger(__name__)

class Classifier(object):
    
    def __init__(self, db, grams=3):
        self.db = db
        self.trigram = Ngrams(grams)

    def train(self, corpus_dir):
        _, langs, _ = os.walk(corpus_dir).next()
        if not langs:
            logger.warning('No languages found under %s', corpus_dir)
        for lang in filter(lambda l: not l.startswith('.'), langs):
            logger.debug('Processing %s', lang)
            file_paths = []
            for root, _, files in os.walk(os.path.join(corpus_dir, lang)):
                file_paths.extend(map(lambda fn: os.path.join(root, fn), files))
            if not file_paths:
                logger.warning('No %s files found under %s', lang, os.path.join(corpus_dir, lang))
            for fpath in file_paths:
                logger.debug('Parsing %s file %s', lang, fpath)
                try:
                    fcontent = open(fpath).read()
                    tokens = tokenize(fcontent)
                    # Errors from generator won't trigger until evaluated,
                    # so enclose the evaluator here
                    map(lambda tok : self.db.put(lang, tok), self.trigram(tokens))
                except UnicodeDecodeError:
                    if fcontent:
                        logger.warning('Cannot decode %s to unicode', fpath)
                    continue
        self.db.save()

    def classify(self, data):
        self.db.load()
        score = collections.defaultdict(lambda :1.0)
        for tok in self.trigram(tokenize(data)):
            for lang in self.db.languages():
                score[lang] *= self.p_lang_on_token(lang, tok)
        return sorted(score.items(), key=lambda s: s[1], reverse=True)

    # TODO, some cache
    def p_token_on_lang(self, token, lang):
        return self.db.c_token_on_lang(token, lang) / self.db.c_tokens_on_lang(lang)

    def p_token(self, token):
        return self.db.c_token(token) / self.db.c_tokens()

    def p_lang(self, lang):
        return self.db.c_tokens_on_lang(lang) / self.db.c_tokens()

    def p_lang_on_token(self, lang, token):
        # P(lang | token) = P(token | lang) * P(lang) / P(token)
        # return self.p_token_on_lang(token, lang) * self.p_lang(lang) / self.p_token(token)
        if not self.db.c_token_on_lang(token, lang) or not self.db.c_token(token):
            # If this token is unseen, its prob should be less than what is seen only once
            logger.debug('%s is not seen in %s, use %f instead', token, lang,
                    0.5/self.db.c_tokens_on_lang(lang))
            return 0.5/self.db.c_tokens_on_lang(lang)
        return self.db.c_token_on_lang(token, lang) / self.db.c_token(token)

if __name__ == '__main__':
    db = DataBase(open('statistics.json'))
    classifier = Classifier(db)
    # classifier.train('corpus')
    print classifier.classify('fdsfdsasafds')

