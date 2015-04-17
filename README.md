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
 2. [The Good-Turing Estimate. CS 6740, Cornell University](http://www.cs.cornell.edu/courses/cs6740/2010sp/guides/lec11.pdf).
