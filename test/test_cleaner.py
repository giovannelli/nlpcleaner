# -*- coding: utf-8 -*-

import pytest

from nlpcleaner import Text

def test_clean_all():
    txt = "dogs playing this      is a test "
    assert Text(txt).clean() == "dog play test"

def test_clear_blank_lines():
    txt = "first line\r\n\r\nsecond line"
    assert Text(txt).clear_blank_lines() == "first line second line"

def test_strip_all():
    txt = "this is a test\n"
    assert Text(txt).strip_all() == "this is a test"

def test_lower_all():
    txt = "THIS IS A TEST"
    assert Text(txt).lower_all() == "this is a test"

def test_remove_numbers():
    txt = "numbers 1 2 3 4 5 6 7 8 9 42"
    assert Text(txt).remove_numbers() == "numbers"

def test_remove_symbols():
    txt = "this is a t風est @#$%"
    assert Text(txt).remove_symbols() == "this is a t風est"

def test_remove_stopwords():
    txt = "this is a test"
    assert Text(txt).remove_stopwords() == "test"

def test_stemming():
    txt = "this is a test"
    assert Text(txt).stemming() == "this is a test"

def test_lemming():
    txt = "this is a test"
    assert Text(txt).lemming() == "this is a test"
