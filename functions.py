from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from nltk.tokenize import word_tokenize
import spacy

# import pandas as pd
from wordcloud import WordCloud
# import matplotlib.pyplot as plt
import io

import pickle

with open("stopwords/stop_words_en.pkl", "rb") as file:
    stop_words_en = pickle.load(file)

with open("stopwords/stop_words_es.pkl", "rb") as file:
    stop_words_es = pickle.load(file)

# stop_words_en = pd.read_pickle("stopwords/stop_words_en.pkl")
# stop_words_es = pd.read_pickle("stopwords/stop_words_es.pkl")
nlp_en = spacy.load("en_core_web_sm")
nlp_es = spacy.load("es_core_news_sm")

# link = "https://www.youtube.com/watch?v=hQMdvrUc1jw"
# link_post = "http://127.0.0.1:5000/return_transcript"
# import requests
# response = requests.post(link_post, json={})
# print(response)
# response.content


def extract_id(link):
    """
    Extracts the video ID from a YouTube video link.

    Parameters:
        link (str): The URL of the YouTube video.

    Returns:
        str: The video ID extracted from the given link.

    Note:
        This function requires the 'parse_qs' and 'urlparse' functions from the 'urllib.parse' module.

    Example:
        link = 'https://www.youtube.com/watch?v=abc12345'  # Replace this with the actual YouTube video link
        video_id = extract_id(link)
        print(f"Extracted Video ID: {video_id}")
    """
    return parse_qs(urlparse(link).query)["v"][0]


def download_script(video_id, language=None, joined_script=True):
    """
    Downloads the transcript script for a YouTube video specified by its video_id.

    Parameters:
        video_id (str): The unique identifier of the YouTube video. It can be found in the video URL after the 'v=' parameter.
        language (str, optional): The language code of the desired transcript. If not provided, the function will fetch the transcript of the first available language.
        joined_script (bool, optional): If True, the function returns the transcript as a single joined string. If False, it returns the original transcript list of dictionaries.

    Returns:
        tuple: A tuple containing the language code and the transcript of the video. If joined_script is True, the transcript will be a single string; otherwise, it will be a list of dictionaries.

    Note:
        This function requires the 'YouTubeTranscriptApi' library to be installed. You can install it using 'pip install youtube-transcript-api'.

    Example:
        video_id = 'abc12345'  # Replace this with the actual YouTube video ID
        language, script = download_script(video_id)
        print(f"Transcript language: {language}")
        print(f"Transcript:\n{script}")
    """
    # video_id = parse_qs(urlparse(link).query)["v"][0]
    if language is None:
        list_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        language = next(iter(list_transcripts)).language_code

    script = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    
    if joined_script:
        word_list = [item["text"] for item in script]
        text = " ".join(word_list)
        return language, text
    else:
        return language, script


def create_wordcloud(
    text,
    language,
    create_file=False,
    filename="wordcloud.png",
):
    """
    Creates a word cloud from the input text, filtering out stop words and lemmatizing words.

    Parameters:
        text (str): The input text from which the word cloud will be generated.
        language (str): The language code of the input text ('es' for Spanish or 'en' for English).
        create_file (bool, optional): If True, the word cloud will be saved as an image file. If False, the function returns the image data.
        filename (str, optional): The filename to be used when saving the word cloud as an image. Applicable only if 'create_file' is True.

    Returns:
        str or bytes: If 'create_file' is True, it returns the filename of the saved word cloud image.
                      If 'create_file' is False, it returns the image data in bytes.

    Note:
        This function requires the 'word_tokenize' from nltk and 'WordCloud' from wordcloud. Ensure that the required dependencies are installed.

    Example:
        text = "This is a sample text containing some words."
        language = "en"
        image_data = create_wordcloud(text, language, create_file=False)
        # Display the word cloud image data (e.g., in a web application)
        display(image_data)
        # Or save the word cloud as an image file
        create_wordcloud(text, language, create_file=True, filename="my_wordcloud.png")
    """
    if language == "es":
        stop_words = stop_words_es
        nlp = nlp_es
    else:
        stop_words = stop_words_en
        nlp = nlp_en

    tokenized = word_tokenize(text)
    tokenized_no_stopwords = [
        word.lower() for word in tokenized if word.lower() not in stop_words
    ]

    text_tokenized = " ".join(tokenized_no_stopwords)
    doc = nlp(text_tokenized)
    lemmas = [tok.lemma_.lower() for tok in doc]
    lemmas_filtered = [
        word.lower() for word in lemmas if word.lower() not in stop_words
    ]

    wordcloud = WordCloud(width=400, height=400).generate(" ".join(lemmas_filtered))

    # BORRAR SI SE VA POR ALTERNATIVA
    # plt.figure(figsize=(8, 8))
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")

    if create_file:
        wordcloud.to_file(filename)
        return filename
    else:
        buffer = io.BytesIO()
        # plt.savefig(buffer, format="png")
        # ALTERNATIVA
        image = wordcloud.to_image()
        image.save(buffer, format='JPEG')
        image_data = buffer.getvalue()
        return image_data
