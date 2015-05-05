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
        a language name and a score.
        """
        self.model.load()
        score = {}
        for lang in self.model.languages():
            probs = []
            for gram in ngram(lex(text), self.grams):
                p = self.p_lang_on_token(lang, gram)
                # We should not use 1.0 as a probability, as it will cause
                # a lot of math errors
                # if p >= 1.0:
                #     p = .999
                probs.append(p)
            # probs.sort(reverse=True)
            score[lang] = self.combined_probability(probs, self.p_lang(lang))
            logger.debug('[%s] probability is %s', lang, self.p_lang(lang))
            logger.debug('[%s] combined probability is %s', lang, score[lang])
        return sorted(score.items(), key=lambda s: s[1], reverse=True)

    # For a good explanation of the background, see:
    # https://www.bionicspirit.com/blog/2012/02/09/howto-build-naive-bayes-classifier.html
    def combined_probability(self, tok_probs, lang_prob):
        """
          P(lang | tok1, tok2, tok3...tokN)
        
          P(tok1, tok2, tok3...tokN | lang) * P(lang)
        = --------------------------------------------
                  P(tok1, tok2, tok3...tokN)

        (naively assume that tokens are independent from each other)

         P(tok1|lang) * P(tok2|lang) * P(tok3|lang) ... P(tokN|lang) * P(lang)
        = ---------------------------------------------------------------------
             P(tok1) * P(tok2) * P(tok3) ... P(tokN)
        
                P(tok|lang)   P(lang|tok)
              ( ----------- = ----------- )
                  P(tok)        P(lang)

         P(lang|tok1) * P(lang|tok2) * P(lang|tok3) ... P(lang|tokN) * P(lang)
        = ---------------------------------------------------------------------
                               P(lang)**N
        """
        # return reduce(lambda x, y: x*y, tok_probs) / (lang_prob**(len(tok_probs)-1))
        # Usually p is not directly computed using the above formula due to 
        # floating-point underflow. Instead, p can be computed in the log domain
        return sum(map(log, tok_probs)) - (len(tok_probs)-1)*log(lang_prob)

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

    def p_lang(self, lang):
        return self.model.n_lang_tokens(lang) / self.model.n_tokens()

if __name__ == '__main__':
    from . import model
    model = model.LanguageModel(open('model.json'))
    classifier = Classifier(model)
    # classifier.train('corpus')
    print classifier.classify('fdsfdsasafds')
