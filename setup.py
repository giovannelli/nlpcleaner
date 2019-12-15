from setuptools import setup

setup(name='nlpcleaner',
      version='0.1',
      description='Clean and prepare text for modeling with machine learning',
      url='https://github.com/giovannelli/nlpcleaner',
      author='Flying Circus',
      author_email='giovannelli@extendi.it',
      license='MIT',
      packages=['nlpcleaner'],
      package_dir={'nlpcleaner': 'src/nlpcleaner'},
      install_requires=[
          'regex',
          'nltk',
          'fasttext',
          'pycountry'
      ],
      zip_safe=False)
