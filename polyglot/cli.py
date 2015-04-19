#!/usr/bin/env python
#coding: utf-8
import os
import sys
import logging
import click

from .db import DataBase
from .classifier import Classifier

logging.basicConfig(format='%(asctime)s -- %(message)s')

@click.group()
def run():
    """I am a computer language savant"""

@run.command()
@click.option('-c', '--corpus', default='corpus', type=click.Path(exists=True),
        help='The corpus folder for training(default corpus).')
@click.option('-n', '--ngram', default=3, type=click.INT,
        help='The size of grams to use, the larger the better, but more expensive(default 3).')
@click.option('-v', '--verbose', is_flag=True, help='Run in debug mode.')
@click.option('-o', '--output', type=click.File('w'), default='-',
        help='File to store training result(default to stdout).')
def train(corpus, ngram, output, verbose):
    """Train polyglot from the corpus folder, each sub-folder represents a language
    which contains many files written in that language(excluding files starting with "." of course)."""
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    if not os.path.isdir(corpus):
        print >> sys.stderr, '%s is not a folder.' % corpus
        return
    db = DataBase(output)
    master = Classifier(db, ngram)
    master.train(corpus)

@run.command()
@click.argument('file', type=click.File('r'))
        # help='Input source code to classify (or standard input if no files are named, or if a single hyphen-minus (-) is given as file name).')
@click.option('-n', '--ngram', default=3, type=click.INT,
        help='The size of grams to use, the larger the better, but more expensive(default 3).')
@click.option('-t', '--top', default=3, type=click.INT,
        help='Output top N most likely language(default 3).')
@click.option('-v', '--verbose', is_flag=True, help='Run in debug mode.')
@click.option('-m', '--model', type=click.File('r', lazy=True), default='model.json',
        help='Language model file which holds the training result(default model.json).')
def classify(file, model, ngram, top, verbose):
    """Do a Naive Bayes classifier on the given FILE, output top N most likely languages"""
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    db = DataBase(model)
    master = Classifier(db, ngram)
    print master.classify(file.read())[:top]

if __name__ == '__main__':
    run()

