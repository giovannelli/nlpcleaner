# Nlpcleaner
Clean and prepare text for modeling with machine learning.

## Usage

```
from nlpcleaner import Text
Text(txt).clean()
```

## Tests

```
pip install .
python setup.py test
```

## Push on PyPi

```
python setup.py sdist
pip install twine
twine upload dist/*
```
