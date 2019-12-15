# -*- coding: utf-8 -*-

import pytest

import nlpcleaner as nc

def test_clean_all():
    assert nc.clean_all("this is a test") == "test"

def test_strip_all():
    assert nc.strip_all("this is a test") == "test"

def test_lower_all():
    assert nc.lower_all("THIS IS A TEST") == "this is a test"

def test_remove_numbers():
    assert nc.remove_numbers("numbers 1 2 3 4 5 6 7 8 9 42") == "numbers"

def test_remove_symbols():
    assert nc.remove_stopwords("this is a test") == "test"

def test_remove_stopwords():
    assert nc.remove_stopwords("this is a test") == "test"

def test_stemming():
    assert nc.remove_stopwords("this is a test") == "test"

def test_lemming():
    assert nc.remove_stopwords("this is a test") == "test"
