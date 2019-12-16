# -*- coding: utf-8 -*-

import pytest

from nlpcleaner import Text

def test_clean_all():
    txt = "Ieri sono andato in due supermercati. Oggi volevo andare all'ippodromo. Stasera mangio la pizza con le verdure."
    assert Text(txt).clean() == "ieri andato due supermercati oggi volevo andare ippodromo stasera mangio pizza verdure"
