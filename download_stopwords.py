import requests
import pickle
import nltk

nltk.download("stopwords")
stopwords = nltk.corpus.stopwords
# import pandas as pd
stop_words_alt_es = requests.get(
    "https://raw.githubusercontent.com/Alir3z4/stop-words/master/spanish.txt"
).text.split("\n")
# stop_words_alt_es = pd.read_csv("https://raw.githubusercontent.com/Alir3z4/stop-words/master/spanish.txt", header=None)[0].to_list()
stop_words_es = set(stopwords.words("spanish")).union(stop_words_alt_es)
with open("stopwords/stop_words_es.pkl", "wb") as pickle_file:
    pickle.dump(stop_words_es, pickle_file)
# pd.to_pickle(stop_words_es, "stopwords/stop_words_es.pkl")

stop_words_alt_en = requests.get(
    "https://raw.githubusercontent.com/Alir3z4/stop-words/master/english.txt"
).text.split("\n")
# stop_words_alt_en = pd.read_csv("https://raw.githubusercontent.com/Alir3z4/stop-words/master/english.txt", header=None)[0].to_list()
stop_words_en = set(stopwords.words("english")).union(stop_words_alt_en)
with open("stopwords/stop_words_en.pkl", "wb") as pickle_file:
    pickle.dump(stop_words_en, pickle_file)
# pd.to_pickle(stop_words_en, "stopwords/stop_words_en.pkl")
