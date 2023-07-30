# from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from nltk.tokenize import word_tokenize
import spacy
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io


stop_words_en = pd.read_pickle("stopwords/stop_words_en.pkl")
stop_words_es = pd.read_pickle("stopwords/stop_words_es.pkl")
nlp_en = spacy.load("en_core_web_sm")
nlp_es = spacy.load("es_core_news_sm")

# link = "https://www.youtube.com/watch?v=hQMdvrUc1jw"
# link_post = "http://127.0.0.1:5000/return_transcript"
# import requests
# response = requests.post(link_post, json={}) 
# print(response)
# response.content
def download_script(video_id, language=None):
    # video_id = parse_qs(urlparse(link).query)["v"][0]
    if language is None:
        list_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        language = next(iter(list_transcripts)).language_code
    
    script = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    word_list = [item["text"] for item in script]
    text = " ".join(word_list)

    return language, text


def create_wordcloud(text,
                     language,
                     create_file=False,
                     filename="wordcloud.png",
                     stop_words_en=stop_words_en,
                     stop_words_es=stop_words_es):
    if language == "es":
        stop_words = stop_words_es
        nlp = nlp_es
    else:
        stop_words = stop_words_en
        nlp = nlp_en
    
    tokenized = word_tokenize(text)
    tokenized_no_stopwords = [word.lower() for word in tokenized
                              if word.lower() not in stop_words]

    text_tokenized = " ".join(tokenized_no_stopwords)
    doc = nlp(text_tokenized)
    lemmas = [tok.lemma_.lower() for tok in doc]
    lemmas_filtered = [word.lower() for word in lemmas
                       if word.lower() not in stop_words]

    # word_counter = pd.Series(lemmas_filtered).value_counts()
    # word_counter = pd.Series(tokenized_no_stopwords).value_counts()
    wordcloud = WordCloud(width=400,
                          height=400).generate(" ".join(lemmas_filtered))

    plt.figure(
        figsize = (8,8)
        )
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    if create_file:
        plt.savefig(filename)
        return filename
    else:
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        image_data = buffer.getvalue()
        return image_data
