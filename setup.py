from setuptools import setup

content= """

nlpcleaner v0.1.1
===================
nlpcleaner is a utility library for text pre processing before generating a model.
`website <https://github.com/giovannelli/nlpcleaner/>`__
=========
-  Text(txt).clean: lower all, strip all, remove numbers, remove symbols, remove stopwords by detected language, apply lemming or stemming
-  stemming & lemmatization are powered by NLTK
    The goal is to make basic cleaning of data hassle free. Most of the
    developers who are working with text data have faced this situation
    where data is not consumable and they end up wasting their time on
    these issues rather than fine tunning the model and get better
    accuracy. In that scenario this library can be useful and save you a
    tone of time.

Tech
~~~~
nplcleaner uses:
-  `NLTK <https://www.nltk.org/>`__ - for advanced cleaning
-  `REGEX <https://pypi.org/project/regex/>`__ - for regular expression

Installation
~~~~~~~~~~~~
textcleaner requires `Python 3.x <https://www.python.org/downloads/>`__
to run.
    pip install nlpcleaner==0.1.1

Usage
~~~~~
.. code:: python
    from nlpcleaner import Text
    Text(txt).clean()

License
-------
MIT
"""

setup(name='nlpcleaner',
      version='0.1.1',
      description='Clean and prepare text for modeling with machine learning',
      long_description=content,
      url='https://github.com/giovannelli/nlpcleaner',
      author='Duccio Giovannelli',
      author_email='giovannelli@extendi.it',
      license='MIT',
      packages=['nlpcleaner'],
      package_dir={'nlpcleaner': 'src/nlpcleaner'},
      install_requires=[
          'regex',
          'nltk>=3.4.5',
          'fasttext>=0.9.1'
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
