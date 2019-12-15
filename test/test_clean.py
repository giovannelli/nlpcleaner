# -*- coding: utf-8 -*-

import pytest

import nlpcleaner as nc

def test_remove_stopwords():
    assert nc.remove_stopwords("this is a test") == "test"
