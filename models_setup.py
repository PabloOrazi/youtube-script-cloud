import pandas as pd
from nltk.corpus import stopwords
import spacy
from spacy.cli import download

stop_words_alt_es = pd.read_csv("https://raw.githubusercontent.com/Alir3z4/stop-words/master/spanish.txt", header=None)[0].to_list()
stop_words_es = set(stopwords.words('spanish')).union(stop_words_alt_es)
pd.to_pickle(stop_words_es, "stopwords/stop_words_es.pkl")
stop_words_alt_en = pd.read_csv("https://raw.githubusercontent.com/Alir3z4/stop-words/master/english.txt", header=None)[0].to_list()
stop_words_en = set(stopwords.words('english')).union(stop_words_alt_en)
pd.to_pickle(stop_words_en, "stopwords/stop_words_en.pkl")

download('en_core_web_sm')
download('es_core_news_sm')
