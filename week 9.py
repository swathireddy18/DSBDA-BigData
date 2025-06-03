import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer


x = open("documents.txt").read()

x

import nltk
nltk.download('punkt_tab')


#Tokenization
tokens = word_tokenize(x)
print(tokens)


import nltk
nltk.download('averaged_perceptron_tagger_eng')

#POS Tagging
postags = pos_tag(tokens)
print(postags)


import nltk
nltk.download('stopwords')


#Removing stop words
stop_words = set(stopwords.words('english'))
print(stop_words)


li = []
for words in tokens:
  if words not in stop_words:
    li.append(words)
print(li)


ps = PorterStemmer()
stemlist = []
for words in li:
  stemlist.append([words, ps.stem(words)])
print(stemlist)



import nltk
nltk.download('wordnet')



#Lemmatization
wl = WordNetLemmatizer()
lemilist = []
for words in li:
  lemilist.append([words, wl.lemmatize(words)])
print(lemilist)
