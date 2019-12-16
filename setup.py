from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='nlpcleaner',
      version='0.1.1',
      description='Clean and prepare text for modeling with machine learning',
      long_description=long_description,
      long_description_content_type='text/markdown',
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
