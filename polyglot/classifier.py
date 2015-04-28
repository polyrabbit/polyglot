#coding: utf-8
from __future__ import division
import os
from math import exp, log

from .lexer import lex, ngram

import logging
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
            file_paths = []
            for root, _, files in os.walk(os.path.join(corpus_dir, lang)):
                file_paths.extend(map(lambda fn: os.path.join(root, fn), files))
            if not file_paths:
                logger.warning('[%s] no file is found under %s', lang, os.path.join(corpus_dir, lang))
            for fpath in file_paths:
                logger.debug('[%s] parsing %s', lang, fpath)
                try:
                    fcontent = open(fpath).read()
                    tokens = lex(fcontent)
                    map(lambda gram: self.model.put(lang, gram), ngram(tokens, self.grams))
                except UnicodeDecodeError:
                    if fcontent:
                        logger.warning('[%s] cannot decode %s to unicode', lang, fpath)
                    continue
        self.model.save()

    def classify(self, text):
        """
        Guess language of the literal text.
        Returns a sorted array of possible languages. Each item contains
        a language name and a confidence level from 0 to 1.
        """
        self.model.load()
        confidence = {}
        for lang in self.model.languages():
            probability_list = []
            for gram in ngram(lex(text), self.grams):
                p = self.p_lang_on_token(lang, gram)
                # We should not use 1.0 as a probability, as it will cause
                # a lot of math errors
                if p >= 1.0:
                    p = .999
                # Neither should an occasional token, as a big chunk of them will
                # counterbalance the discriminating ones
                # elif p < .0001:
                #     continue
                probability_list.append(p)
            # probability_list.sort(reverse=True)
            confidence[lang] = self.combined_probability(probability_list)
            logger.debug('[%s] combined probability is %s', lang, confidence[lang])
        return sorted(confidence.items(), key=lambda s: s[1], reverse=True)

    # For a good explanation of the background, see:
    # http://blog.csdn.net/hexinuaa/article/details/5596862
    def combined_probability(self, probability_list):
        def prod(iterable):
            """
            To avoid floating underflow, we multiply a scale
            """
            if not iterable:
                return 0, 1
            scale = 1
            pi = 1.0
            for x in iterable:
                pi *= x
                while pi <= 1e-10:
                    pi *= 1e10
                    scale *= 1e10
            return pi, scale

        # return 1.0/(prod([1/p-1 for p in probability_list])+1)
        # Damn floating underflow
        prod_of_probability, s1 = prod(probability_list)
        prod_of_complementing_probability, s2 = prod([1-p for p in probability_list])
        # try:
        return prod_of_probability / (prod_of_probability + prod_of_complementing_probability*(s1/s2))
        # except ZeroDivisionError:
        #     # We have a floating-point underflow
        #     return 0

        # Opt 2: Usually p is not directly computed using the above formula
        # due to floating-point underflow. Instead, p can be computed in the log domain
        # p = 1 / (1 + e**eta) where eta equals sum(ln(1-p[i])-ln(p[i]) i=1,2,3...N
        # see http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering
        eta = sum(log(1-pi)-log(pi) for pi in probability_list)
        # Since the probability is in inverse proportion to eta,
        # we just return -eta to avoid OverflowError error
        return -eta
        # return 1.0 / (1 + exp(eta))

    def p_lang_on_token(self, lang, token):
        """"
        Probability of a language given a token
        P(lang | token) = P(token | lang) * P(lang) / P(token)

           n_token_on_lang(token, lang)     n_lang_tokens(lang)     n_token(token)
        = ------------------------------ * -------------------- /  ---------------
           n_lang_tokens(lang)              n_tokens()              n_tokens()

           n_token_on_lang(token, lang) 
        = ------------------------------
           n_token(token)
        """
        if not self.model.n_token_on_lang(token, lang):
            # A crude smoothing algo
            logger.debug('[%s] %s is not seen, use %s instead', lang, token,
                    1.0/(self.model.n_tokens()+1))
            return 1.0/(self.model.n_tokens()+1)
        p = self.model.n_token_on_lang(token, lang) / self.model.n_token(token)
        logger.debug('[%s] probability given %s is %s', lang, token, p)
        return p

if __name__ == '__main__':
    from . import model
    model = model.LanguageModel(open('model.json'))
    classifier = Classifier(model)
    # classifier.train('corpus')
    print classifier.classify('fdsfdsasafds')
