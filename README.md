polyglot
========

[![Build Status](https://travis-ci.org/polyrabbit/polyglot.svg?branch=master)](https://travis-ci.org/polyrabbit/polyglot)

Program language savant. It is used to detect program languages just like [github/linguist](https://github.com/github/linguist/), but based on a statistical model.

### Getting Started
Install using pip

```
pip install git+https://github.com/polyrabbit/polyglot
```

First, we need to train polyglot on a multilingual training corpus, each folder in the corpus should contain files of the same language whose name is identified by the folder. e.g.
```
polyglot train --corpus=./corpus --ngram=3 --verbose --output=./model.json
```

Run `polyglot train --help` for usage specifics.

After training, we can use the Naive Bayes classifier to classify a given file. e.g.
```
echo import os | polyglot classify --ngram=3 --top=3 --verbose --model=./model.json -
```
Which outputs top 3 most likely languages in descending order with their scores `[(u'Python', 6.719828065958895), (u'Frege', -11.021531184412824), (u'Objective-C++', -13.244791737113022)]`
Run `polyglot classify --help` for usage specifics.

### Algorithm

1. Computing the probability that a message containing a given word is spam
2. The spamicity of a word
3. Combining individual probabilities
4. Other expression of the formula for combining individual probabilities
5. Dealing with rare words
6. Other heuristics
7. Mixed methods

### References
 1. [A Plan For Spam](http://www.paulgraham.com/spam.html).
 2. [Naive Bayes spam filtering](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering).
 3. [Implementation of naive bayesian spam filter algorithm](http://blog.csdn.net/hexinuaa/article/details/5596862).
 4. [How To Build a Naive Bayes Classifier](https://www.bionicspirit.com/blog/2012/02/09/howto-build-naive-bayes-classifier.html).
