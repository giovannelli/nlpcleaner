import os
import regex as re,string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import fasttext
from pycountry import languages

# Set nltk folder
nltk.data.path.append(os.getcwd() + "/src/data/nltk")
# Load languages models
languages_model = fasttext.load_model(os.getcwd() + "/src/data/fasttext/lid.176.ftz")

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

# Cleanup all
def clean_all(corpus):
    corpus = lower_all(corpus)
    return corpus

# converts each character to lowercase
def lower_all(corpus):
    lowered = [each.lower() for each in corpus]
    return "".join(lowered)

# removes all the blank line from the text file
# returns list
def clear_blank_lines(corpus):
    return list(filter(str.strip,[each.rstrip() for each in corpus]))

# it removes ".\n" from every element by default
# can be used to strip by second argument
def strip_all(corpus, x='.\n'):
    stripped = [re.sub(r'\s+',' ', each.strip(x)) for each in corpus]
    return "".join(stripped)

# removes numbers detected anywhere in the data
def remove_numbers(corpus):
    no_numbers = re.sub(r'[0-9]+','',(each)) for each in corpus
    print("Siamo nel no")
    print(no_numbers)
    return "".join(no_numbers).strip(' ')

# removes punctuations detected anywhere in the data
def remove_symbols(corpus):
    no_symbols = [re.sub(r'[^\w\s]','',each) for each in corpus]
    return "".join(no_symbols)

# it will remove stop words and return a list of list of words
def remove_stopwords(corpus):
    no_stopwords = [w for w in corpus.split() if not w in stop_words["en"]]
    return "".join(no_stopwords)

# reduces each word to its stem work like, dogs to dog
def stemming(corpus):
    corpus = [[stemmer.stem(word) for word in each.split()] for each in corpus]
    return " ".join(corpus)

# gets the root word for each word
def lemming(corpus):
    corpus = [[lemmatizer.lemmatize(word) for word in each.split()] for each in corpus]
    return " ".join(corpus)
