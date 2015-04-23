#coding: utf-8
from __future__ import division
import os
import collections
import logging

from .lexer import lex, ngram

logger = logging.getLogger(__name__)

class Classifier(object):
    """Bayesian classifier. """

    def __init__(self, model, grams=3):
        self.model = model
        self.grams = grams

    def train(self, corpus_dir):
        """
        Pass in a directory containing sample language files.
        Returns None
        """
        _, langs, _ = os.walk(corpus_dir).next()
        if not langs:
            logger.warning('No language is found under %s', corpus_dir)
        for lang in filter(lambda l: not l.startswith('.'), langs):
            logger.debug('Processing %s', lang)
            file_paths = []
            for root, _, files in os.walk(os.path.join(corpus_dir, lang)):
                file_paths.extend(map(lambda fn: os.path.join(root, fn), files))
            if not file_paths:
                logger.warning('No %s file is found under %s', lang, os.path.join(corpus_dir, lang))
            for fpath in file_paths:
                logger.debug('Parsing %s file %s', lang, fpath)
                try:
                    fcontent = open(fpath).read()
                    tokens = lex(fcontent)
                    map(lambda gram: self.model.put(lang, gram), ngram(tokens, self.grams))
                except UnicodeDecodeError:
                    if fcontent:
                        logger.warning('Cannot decode %s to unicode', fpath)
                    continue
        self.model.save()

    def classify(self, text):
        """
        Guess language of the literal text.
        Returns a sorted array of possible languages. Each item contains
        a language name and a confidence level from 0 to 1.
        """
        self.model.load()
        confidence = collections.defaultdict(lambda: 1.0)
        for lang in self.model.languages():
            probability_list = []
            for gram in ngram(lex(text), self.grams):
                probability_list.append(self.p_lang_on_token(lang, gram))
            confidence[lang] = self.combined_probability(probability_list)
        return sorted(confidence.items(), key=lambda s: s[1], reverse=True)

    def combined_probability(self, probability_list):
        def prod(iterable):
            return reduce(lambda x, y: x*y, iterable, 1.0)

        prod_of_probability = prod(probability_list)
        prod_of_complementing_probability = prod([1-p for p in probability_list])
        return prod_of_probability / (prod_of_probability + prod_of_complementing_probability)

    # TODO, some cache
    def p_token_on_lang(self, token, lang):
        """
        Probability of a token given a language
        P(lang | token)
        """
        return self.model.c_token_on_lang(token, lang) / self.model.c_lang_tokens(lang)

    def p_token(self, token):
        return self.model.c_token(token) / self.model.c_tokens()

    def p_lang(self, lang):
        """
        Probability of a language
        """
        return self.model.c_lang_tokens(lang) / self.model.c_tokens()

    def p_lang_on_token(self, lang, token):
        """"
        Probability of a language given a token
        P(lang | token) = P(token | lang) * P(lang) / P(token)
        = c_token_on_lang(token, lang) / c_lang_tokens(lang)
            * c_lang_tokens(token) / c_tokens()
            / (c_token(token) / c_tokens() )
        = c_token_on_lang(token, lang) / c_lang_tokens(lang)
        """
        if not self.model.c_token_on_lang(token, lang):
            # A crude smoothing algo
            logger.debug('%s is not seen in %s, use %f instead', token, lang,
                    1.0/(self.model.c_lang_tokens(lang)+1))
            return 1.0/(self.model.c_lang_tokens(lang)+1)
        return self.model.c_token_on_lang(token, lang) / self.model.c_token(token)

if __name__ == '__main__':
    from . import model
    model = model.LanguageModel(open('model.json'))
    classifier = Classifier(model)
    # classifier.train('corpus')
    print classifier.classify('fdsfdsasafds')

