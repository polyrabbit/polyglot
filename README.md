polyglot
========

Program language savant

### Getting Started
Install using pip

```
pip install git+https://github.com/polyrabbit/polyglot
```

First, we need to train polyglot on a multilingual training corpus, each folder in the corpus should contain files of the same language whose name is identified by the folder. Run `polyglot train --help` for usage specifics.

After training, we can use the Naive Bayes classifier to classify a given file. Run `polyglot classify --help` for usage specifics.

### References
 1. [A Plan For Spam](http://www.paulgraham.com/spam.html).
 2. [Naive Bayes spam filtering](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering).
 3. [Implementation of naive bayesian spam filter algorithm](http://blog.csdn.net/hexinuaa/article/details/5596862).
 4. [How To Build a Naive Bayes Classifier](https://www.bionicspirit.com/blog/2012/02/09/howto-build-naive-bayes-classifier.html).
