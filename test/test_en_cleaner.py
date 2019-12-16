# -*- coding: utf-8 -*-

import pytest

from nlpcleaner import Text

def test_clean_all():
    txt = "MANY dogs enjoy tug and chew toys and playing 'hide and seek' with you outdoors"
    assert Text(txt).clean() == "many dog enjoy tug chew toy playing hide seek outdoors"

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
    txt = "this is a t風est `~!@#$%^&*()_|+\-=?;:'\",.<>{}[]/"
    assert Text(txt).remove_symbols() == "this is a t風est"

def test_remove_stopwords():
    txt = "this is a test"
    assert Text(txt).remove_stopwords() == "test"

def test_stemming():
    txt = "many dogs enjoy tug and chew toys and playing 'hide and seek' with you outdoors"
    assert Text(txt).stemming() == "mani dog enjoy tug and chew toy and play hide and seek with you outdoor"

def test_lemming():
    txt = "many dogs enjoy tug and chew toys and playing 'hide and seek' with you outdoors"
    assert Text(txt).lemming() == "many dog enjoy tug and chew toy and playing 'hide and seek' with you outdoors"
