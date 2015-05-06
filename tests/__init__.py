import unittest
import os
from polyglot.model import LanguageModel
from polyglot.classifier import Classifier
import cStringIO
from time import time

import logging
logging.basicConfig(format='%(asctime)s -- %(message)s', level=logging.INFO)

class TestShit(unittest.TestCase):
    ngram = 3
    corpus_dir = './corpus'
    model_fp = cStringIO.StringIO()
    # model_fp = open('../model.json')

    def test_corpus(self):

        print 'Training',
        db = LanguageModel(self.model_fp)
        god = Classifier(db, self.ngram)
        god.train(self.corpus_dir)
        print 'done'

        _, langs, _ = os.walk(self.corpus_dir).next()
        for lang in filter(lambda l: not l.startswith('.'), langs):
            file_paths = []
            for root, _, files in os.walk(os.path.join(self.corpus_dir, lang)):
                file_paths.extend(map(lambda fn: os.path.join(root, fn), files))
            for fpath in file_paths:
                print fpath,
                ts = time()
                self.assertEqual(god.classify(open(fpath).read())[0][0], lang)
                print 'passed, took: %2.4f sec' % (time()-ts)

if __name__ == '__main__':
    unittest.main()

