#coding: utf-8
from __future__ import unicode_literals
import sys
import StringIO
import logging
# A monkey patch to ensure cStringIO support unicode
sys.modules['cStringIO'] = StringIO
from shlex import shlex
from collections import deque
from chardet import detect

logger = logging.getLogger(__name__)

class Ngrams(object):
    def __init__(self, n):
        self.n = n

    def __call__(self, iterable):
        last_grams = deque(maxlen=self.n)
        for ite in iterable:
            last_grams.append(ite)
            _last_grams = tuple(last_grams)
            for i in xrange(len(_last_grams)):
                yield _last_grams[i:self.n]

def lex(text):
    if not isinstance(text, unicode):
        ie = detect(text)['encoding']
        if not ie:
            raise UnicodeDecodeError(b'oops', b'Unknown encoding', 0, 1, text)
        text = text.decode(ie)
    for token in text.split():  #TODO, shit! abap use " as its comment
    # for token in shlex(text):
    # for token in shlex(text.replace('"""', '"').replace("'''", "'")):  # For python
        if token.isdigit():
            continue
        # elif token.startswith(('"', "'")):
        #     yield token[1:-1]
        else:
            yield token

if __name__ == '__main__':
    assert list(lex('aa "ss" 23我')) == ['aa', '"ss"', u'我']
    assert len(list(Ngrams(3)(xrange(7)))) == 1+2+3*5
