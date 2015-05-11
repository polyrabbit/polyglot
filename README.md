polyglot
========

[![Build Status](https://travis-ci.org/polyrabbit/polyglot.svg?branch=master)](https://travis-ci.org/polyrabbit/polyglot)

Program language savant. It is used to detect program languages just like [github/linguist](https://github.com/github/linguist/), but based on naive Bayes classifier.

### Getting Started
Install using pip

```
pip install git+https://github.com/polyrabbit/polyglot
```

First, we need to train polyglot on a multilingual training corpus, each folder in the corpus should contain files of the same language whose name is identified by the folder. e.g.
```
polyglot train --corpus=./corpus --ngram=3 --verbose --output=./model.json
```

A pre-included [model.json](https://github.com/polyrabbit/polyglot/blob/master/model.json) is generated using the above command. Run `polyglot train --help` for usage specifics.

After training, we can use the Naive Bayes classifier to classify a given file. e.g.
```
echo import os | polyglot classify --ngram=3 --top=3 --verbose --model=./model.json -
```
Which outputs top 3 most likely languages in descending order with their scores 

```
[(u'Python', 6.719828065958895), (u'Frege', -11.021531184412824), (u'Objective-C++', -13.244791737113022)]
```
Run `polyglot classify --help` for usage specifics.

### Classification Algorithm

1. Lex input string into tokens, and generate n-grams from those tokens (trigram by default)


        "#include<stdio.h>".lex().ngram(max_n=3)
        
        =>[['#'], ['include'], ['<'], ['stdio'], ['.'], ['h'], ['>'], ['#', 'include'], ['include', '<'], ['<', 'stdio'], ['stdio', '.'], ['.', 'h'], ['h', '>'], ['#', 'include', '<'], ['include', '<', 'stdio'], ['<', 'stdio', '.'], ['stdio', '.', 'h'], ['.', 'h', '>']]


2. Computing the probability of a language given a token


        P(lang | token) 
        
        = P(token | lang) * P(lang) / P(token)

           n_token_on_lang(token, lang)     n_lang_tokens(lang)     n_token(token)
        = ------------------------------ * -------------------- /  ---------------
           n_lang_tokens(lang)              n_tokens()              n_tokens()

           n_token_on_lang(token, lang) 
        = ------------------------------
           n_token(token)


3. Combining individual probabilities


   		P(lang | tok_1, tok_2, tok_3...tok_n)
   		
          P(tok_1, tok_2, tok_3...tok_n | lang) * P(lang)
        = --------------------------------------------
                  P(tok_1, tok_2, tok_3...tok_n)

          (naively assume that tokens are independent from each other)

          P(tok_1|lang) * P(tok_2|lang) * P(tok_3|lang) ... P(tok_n|lang) * P(lang)
        = ---------------------------------------------------------------------
             P(tok_1) * P(tok_2) * P(tok_3) ... P(tok_n)
        
                P(tok|lang)   P(lang|tok)
              ( ----------- = ----------- )
                  P(tok)        P(lang)

          P(lang|tok_1) * P(lang|tok_2) * P(lang|tok_3) ... P(lang|tok_n) * P(lang)
        = ---------------------------------------------------------------------
                               P(lang)^N

5. Dealing with rare words


		P(unseen_token) = 1.0/(n_all_tokens()+1)


### References
 1. [A Plan For Spam](http://www.paulgraham.com/spam.html)
 2. [Naive Bayes spam filtering](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)
 3. [Implementation of naive bayesian spam filter algorithm](http://blog.csdn.net/hexinuaa/article/details/5596862)
 4. [How To Build a Naive Bayes Classifier](https://www.bionicspirit.com/blog/2012/02/09/howto-build-naive-bayes-classifier.html)

[V2EX讨论](https://www.v2ex.com/t/190152)