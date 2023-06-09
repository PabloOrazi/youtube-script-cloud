from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# link = "https://www.youtube.com/watch?v=hQMdvrUc1jw"
# link_post = "http://127.0.0.1:5000/return_transcript"
# import requests
# response = requests.post(link_post, json={}) 
# print(response)
# response.content


def download_script(link, language=None):
    video_id = parse_qs(urlparse(link).query)["v"][0]
    if language is None:
        list_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        language = next(iter(list_transcripts)).language_code

    script = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    word_list = [item["text"] for item in script]
    text = " ".join(word_list)

    return text

# lista = [item["text"] for item in script]

# texto = " ".join(lista)
# tokenizado = word_tokenize(texto)
# stop_words = set(stopwords.words('spanish'))
# stop_words_alt = pd.read_csv("https://raw.githubusercontent.com/Alir3z4/stop-words/master/spanish.txt", header=None)[0].to_list()
# stop_words = stop_words.union(stop_words_alt)

tokenizado_filtrado_stop_words = [palabra.lower() for palabra in tokenizado if palabra.lower() not in stop_words]

import pkg_resources,imp
imp.reload(pkg_resources)
import spacy
nlp = spacy.load("es_core_news_sm")
text = " ".join(tokenizado_filtrado_stop_words)
doc = nlp(text)

lemmas = [tok.lemma_.lower() for tok in doc]
lemmas_filtrado = [palabra.lower() for palabra in lemmas if palabra.lower() not in stop_words]

import pandas as pd
contador_palabras = pd.Series(lemmas_filtrado).value_counts()
contador_palabras

from wordcloud import WordCloud
wordcloud = WordCloud(width=800, height=600).generate(" ".join(lemmas_filtrado))

import matplotlib.pyplot as plt
plt.figure(figsize = (18,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")