#coding: utf-8
from __future__ import unicode_literals
import sys
import StringIO
import logging
# A monkey patch to ensure cStringIO support unicode
sys.modules['cStringIO'] = StringIO
import re
from shlex import shlex
from collections import deque
from functools32 import lru_cache
from chardet import detect

logger = logging.getLogger(__name__)

# Expression to match some_token and some_token="with spaces" (and similarly
# for single-quoted strings).
# Shamelessly steal from https://github.com/django/django/blob/master/django/utils/text.py#L335
lexer_patt = re.compile(r""" 
    (?:  # ignore strings
        \w* 
        (?: 
            (?:"(?:[^"\\\n]|\\.)*" | '(?:[^'\\\n]|\\.)*') 
            \w* 
        )+ 
    ) | (?P<tok>\w+ 
    | \S) 
""", re.VERBOSE)

def ngram(tokens, max_n, min_n=1):
    """
    Yields n-grams from a tokens
    see http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
    >>> list(ngram([1, 2, 3, 4], 3, 1))
    [(1,), (2,), (3,), (4,), (1, 2), (2, 3), (3, 4), (1, 2, 3), (2, 3, 4)]
    """
    tokens = tuple(tokens)
    for i in range(min_n, max_n+1):
        for grams in zip(*[tokens[j:] for j in range(i)]):
            yield grams

@lru_cache(maxsize=1)
def lex(text):
    """Yields a list of tokens from a given text."""
    if not isinstance(text, unicode):
        ie = detect(text)['encoding']
        if not ie:
            raise UnicodeDecodeError(b'oops', b'Unknown encoding', 0, 1, text)
        text = text.decode(ie)
    # for token in text.split():  #TODO, shit! abap use " as its comment
    ret = []
    for token_group in lexer_patt.finditer(text):
    # for token in shlex(text):
    # for token in shlex(text.replace('"""', '"').replace("'''", "'")):  # For python
        token = token_group.group('tok')
        if token is None:
            continue
        if token.isdigit():
            continue
        # elif token.startswith(('"', "'")) or token.endswith(('"', "'")):
        #     continue
        else:
            # For the sake of cache
            # yield token
            ret.append(token)
    return ret

if __name__ == '__main__':
    assert list(lex('aa "ss" 23我')) == ['aa', u'我']
    assert len(list(ngram(xrange(7), 3))) == 1+2+3*5
