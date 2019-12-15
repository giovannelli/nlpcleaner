import os
import regex as re,string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import fasttext
from pycountry import languages

from text_cleaner import __version__

__author__ = "Duccio Giovannelli"
__copyright__ = "Duccio Giovannelli"
__license__ = "mit"

nltk.data.path.append(os.getcwd() + "/src/data/nltk")
languages_model = fasttext.load_model(os.getcwd() + "/src/data/fast_text/lid.176.ftz")

stop_words = {}
stop_words['ar'] = set(stopwords.words('arabic'))
stop_words['az'] = set(stopwords.words('azerbaijani'))
stop_words['da'] = set(stopwords.words('danish'))
stop_words['nl'] = set(stopwords.words('dutch'))
stop_words['en'] = set(stopwords.words('english'))
stop_words['fi'] = set(stopwords.words('finnish'))
stop_words['fr'] = set(stopwords.words('french'))
stop_words['de'] = set(stopwords.words('german'))
stop_words['el'] = set(stopwords.words('greek'))
stop_words['hu'] = set(stopwords.words('hungarian'))
stop_words['id'] = set(stopwords.words('indonesian'))
stop_words['it'] = set(stopwords.words('italian'))
stop_words['kk'] = set(stopwords.words('kazakh'))
stop_words['ne'] = set(stopwords.words('nepali'))
stop_words['nn'] = set(stopwords.words('norwegian'))
stop_words['pt'] = set(stopwords.words('portuguese'))
stop_words['ro'] = set(stopwords.words('romanian'))
stop_words['ru'] = set(stopwords.words('russian'))
stop_words['sl'] = set(stopwords.words('slovene'))
stop_words['es'] = set(stopwords.words('spanish'))
stop_words['sv'] = set(stopwords.words('swedish'))
stop_words['tg'] = set(stopwords.words('tajik'))
stop_words['tr'] = set(stopwords.words('turkish'))

stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()


def clean(corpus):
    print("clening")
