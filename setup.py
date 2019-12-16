from setuptools import setup

setup(name='nlpcleaner',
      version='0.1.1',
      description='Clean and prepare text for modeling with machine learning',
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
