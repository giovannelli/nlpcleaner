import os
import regex as re,string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import fasttext # to detect language

# Stemmer:
# Danish
# Dutch
# English
# Finnish
# French
# German
# Hungarian
# Italian
# Norwegian
# Porter
# Portuguese
# Romanian
# Russian
# Spanish
# Swedish

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

class Text:
    def __init__(self, corpus):
      self.corpus = corpus

    def clean(self):
      cleaned = self.__lower_all()\
                    .__clear_blank_lines()\
                    .__strip_all()\
                    .__remove_numbers()\
                    .__remove_symbols()\
                    .__remove_stopwords()\
                    .__stemming()\
                    .__lemming()\
                    .__formatting().corpus
      return cleaned

    def tokenized(self):
        words = filter(lambda x: len(x)>0, self.corpus.split(' '))
        return words

    def lower_all(self):
        return self.__lower_all()\
                   .__formatting().corpus

    def clear_blank_lines(self):
        return self.__clear_blank_lines()\
                   .__formatting().corpus

    def strip_all(self):
        return self.__strip_all()\
                   .__formatting().corpus

    def remove_numbers(self):
        return self.__remove_numbers()\
                   .__formatting().corpus

    def remove_symbols(self):
        return self.__remove_symbols()\
                   .__formatting().corpus

    def remove_stopwords(self):
        return self.__remove_stopwords()\
                   .__formatting().corpus

    def stemming(self):
        return self.__stemming()\
                   .__formatting().corpus

    def lemming(self):
        return self.__lemming()\
                   .__formatting().corpus

    # converts each character to lowercase
    def __lower_all(self):
        self.corpus = ''.join([each.lower() for each in self.corpus])
        return self

    # removes all the blank line from the text file
    def __clear_blank_lines(self):
        self.corpus = re.sub(r'\r\n', ' ', self.corpus)
        return self

    # it removes ".\n" from every element by default
    # can be used to strip by second argument
    def __strip_all(self):
        self.corpus = re.sub(r'\n', ' ', self.corpus)
        return self

    # removes numbers detected anywhere in the data
    def __remove_numbers(self):
        self.corpus = re.sub(r'[0-9]+',' ',self.corpus)
        return self

    # removes punctuations detected anywhere in the data
    def __remove_symbols(self):
        self.corpus = re.sub(r'[^\w\s]','',self.corpus)
        return self

    # it will remove stop words and return a list of list of words
    def __remove_stopwords(self):
        self.corpus = ' '.join([w for w in self.corpus.split() if not w in stop_words["en"]])
        return self

    # reduces each word to its stem work like, dogs to dog
    def __stemming(self):
        words = self.tokenized()
        stem_sentence=[]
        for word in words:
            stem_sentence.append(stemmer.stem(word))
            stem_sentence.append(' ')
        self.corpus = ''.join(stem_sentence)
        return self

    # gets the root word for each word
    def __lemming(self):
        words = self.tokenized()
        lem_sentence=[]
        for word in words:
            lem_sentence.append(lemmatizer.lemmatize(word))
            lem_sentence.append(' ')
        self.corpus = ''.join(lem_sentence)
        return self

    # apply common format to all responses
    # - remove double spaces
    def __formatting(self):
        self.corpus = re.sub(r'\s\s+',' ',self.corpus).strip()
        return self
