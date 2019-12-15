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
    print("aaaa")

# class document:

#     file_name = ''
#     data = []
#     words = []
#     tokens = []
#     count_sentences = 0
#     count_words = 0
#     each_word_count = {}

#     def __init__(self,fname=''):
#         language = languages_model.predict('الشمس تشرق', k=1)[0][0].split("__")[-1]
#         language_name = languages.get(alpha_2=language).name.lower()

#         if fname:
#             self.data,fame =  self._reader(fname)
#             self.words = [each.split(' ') for each in self.clear_blank_lines().lower_all().strip_all().remove_numbers().remove_symbols()]
#             self.count_words = len([word for sent in self.words for word in sent])
#             self.count_sentences = sum(each.count('.') for each in self.data)
#             temp = self._flatlist(self.words)
#             self.each_word_count = {x:temp.count(x) for x in temp}
#             self.file_name = fame.split('\\')[-1]
#         else:
#             pass

#     def _flatlist(self,lis):
#         return [word for sent in lis for word in sent]

#     def __repr__(self):
#          return '\n'.join(map(str, self.data))

#     def __str__(self):
#         return '\n'.join(map(str, self.data))

#     def __iter__(self):
#         for i in self.data: yield i

#     def copy(self):
#         temp = copy.deepcopy(self)
#         return temp

#     # checks whether it has file path as argument
#     def _file_or_not(self,arg):
#         if os.path.isfile(arg):
#             return True
#         else:
#             return False,"only supports .txt for now"

#     # this reader is flexible enough to process file or will return the data if list is being passed to the function.
#     def _reader(self,file):
#         if type(file)==str and self._file_or_not(file)==True:
#             with open(file,'r') as f:
#                 return f.readlines(),file

#         elif type(file)==str:
#             return file.split('\n'),''

#         else: return file,''



#     #removes all the blank line from the text file
#     #returns list
#     def clear_blank_lines(self,inplace=False):
#         if not inplace: self = self.copy()
#         self.data =  list(filter(str.strip,[each.rstrip() for each in self.data]))
#         return self


#     # it removes ".\n" from every element by default
#     # can be used to strip by second argument
#     def strip_all(self,x='.\n',inplace=False):
#         if not inplace: self = self.copy()
#         self.data = [re.sub(r'\s+',' ',each.strip(x)) for each in self.data]
#         return self


#     # converts each character to lowercase
#     def lower_all(self,inplace=False):
#         if not inplace: self = self.copy()
#         self.data = [each.lower() for each in self.data]
#         return self

#     # removes numbers detected anywhere in the data
#     def remove_numbers(self,inplace=False):
#         if not inplace: self = self.copy()
#         self.data = [re.sub(r'[0-9]+', '',(each)) for each in self.data]
#         return self

#     # removes punctuations detected anywhere in the data
#     def remove_symbols(self,inplace=False):
#         if not inplace: self = self.copy()
#         self.data = [re.sub(r'[^\w\s]','',each) for each in self.data]
#         return self.strip_all()


#     # it will remove stop words and return a list of list of words
#     def remove_stpwrds(self,inplace=False):
#         if not inplace: self = self.copy()
#         self.words = [[w for w in each.split() if not w in stop_words] for each in self.data]

#         self.data = formating(self.words)
#         return self


#     #for tokenization this function can't be use as object
#     def token_it(self):
#         self.tokens = [word_tokenize(each) for each in self.data]
#         return self.tokens

#     # reduces each word to its stem work like, dogs to dog
#     def stemming(self,inplace=False):
#         if not inplace: self = self.copy()
#         self.data = formating([[stemmer.stem(word) for word in each.split()] for each in self.data])
#         return self

#     # gets the root word for each word
#     def lemming(self,inplace=False):
#         if not inplace: self = self.copy()
#         self.data = formating([[lemmatizer.lemmatize(word) for word in each.split()] for each in self.data])
#         return self


#     def main_cleaner(self,op = 'sents',inplace=False):
#         if not inplace: self = self.copy()

#         # this is the basic cleaning which operates with each line
#         part1 = self.clear_blank_lines().strip_all().lower_all().remove_numbers().remove_symbols()

#         # this is the advanced cleaning which operates with each word
#         part2 = part1.lemming().remove_stpwrds()

#         if op== 'sents':
#             return part2

#         if op== 'words':
#             return [word for sent in part2.data for word in sent.split()]

#         if op not in ('sents','words'):
#             return "value of option is not valid, try 'sents' or 'words' instead"
