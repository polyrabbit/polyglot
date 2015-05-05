import unittest
import os
from polyglot.model import LanguageModel
from polyglot.classifier import Classifier
import cStringIO

import logging
logging.basicConfig(format='%(asctime)s -- %(message)s', level=logging.DEBUG)

class TestShit(unittest.TestCase):
    ngram = 3
    corpus_dir = './corpus'
    model_fp = cStringIO.StringIO()

    def train(self):
        print 'Training'
        db = LanguageModel(self.model_fp)
        master = Classifier(db, self.ngram)
        master.train(self.corpus_dir)
        print 'Train done'

    def test_corpus(self):
        self.train()

        _, langs, _ = os.walk(self.corpus_dir).next()
        for lang in filter(lambda l: not l.startswith('.'), langs):
            file_paths = []
            for root, _, files in os.walk(os.path.join(self.corpus_dir, lang)):
                file_paths.extend(map(lambda fn: os.path.join(root, fn), files))
            for fpath in file_paths:
                self.model_fp.seek(0)
                db = LanguageModel(self.model_fp)
                master = Classifier(db, self.ngram)
                self.assertEqual(master.classify(open(fpath).read())[0][0], lang)

if __name__ == '__main__':
    unittest.main()

