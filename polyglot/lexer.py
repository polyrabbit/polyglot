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

def ngram(iterable, max_n, min_n=1):
    """
    Yields n-grams from a iterable
    see http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
    >>> list(ngram([1, 2, 3, 4], 3, 1))
    [(1,), (2,), (3,), (4,), (1, 2), (2, 3), (3, 4), (1, 2, 3), (2, 3, 4)]
    """
    iterable = tuple(iterable)
    for i in range(min_n, max_n+1):
        for grams in zip(*[iterable[j:] for j in range(i)]):
            yield grams

def lex(text):
    """Yields a list of tokens from a given text."""
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
    assert len(list(ngram(xrange(7), 3))) == 1+2+3*5
