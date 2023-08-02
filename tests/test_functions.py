import os
import pytest
from functions import extract_id, download_script, create_wordcloud


def test_extract_id_valid_link():
    link = "https://www.youtube.com/watch?v=abc12345"
    expected_id = "abc12345"
    extracted_id = extract_id(link)
    assert extracted_id == expected_id


def test_extract_id_invalid_link():
    # Testing with a link without the 'v' parameter
    link = "https://www.youtube.com/watch?param=value"
    with pytest.raises(KeyError):
        extract_id(link)


def test_extract_id_empty_link():
    # Testing with an empty link
    link = ""
    with pytest.raises(KeyError):
        extract_id(link)


def test_extract_id_no_query_parameter():
    # Testing with a link without any query parameters
    link = "https://www.youtube.com/watch"
    with pytest.raises(KeyError):
        extract_id(link)


def test_download_script_with_default_language():
    # Test download_script with default language (should fetch the first available transcript)
    video_id = "OJDkPz3nPjM"
    language, script = download_script(video_id)
    assert isinstance(language, str)
    assert language == "en"
    assert isinstance(script, str)
    assert (
        script
        == "- To deal with this problem\nof the two Americas, we are seeking to make America one nation, indivisible, with liberty\nand justice for all."
    )


def test_download_script_with_list_returned():
    # Test download_script with joined_script=False (should return a list of dictionaries)
    video_id = "OJDkPz3nPjM"
    language, script_list = download_script(video_id, joined_script=False)
    assert isinstance(language, str)
    assert language == "en"
    assert isinstance(script_list, list)
    assert all(isinstance(item, dict) for item in script_list)


def test_create_wordcloud_without_saving():
    # Test create_wordcloud with create_file=False
    text = "This is a sample text containing some words."
    language = "en"
    image_data = create_wordcloud(text, language, create_file=False)

    # Assert that the output is bytes (image data)
    assert isinstance(image_data, bytes)


def test_create_wordcloud_without_saving_in_spanish():
    # Test create_wordcloud with create_file=False and spanish language
    text = "Este es un texto ejemplo que contiene algunas palabras."
    language = "es"
    image_data = create_wordcloud(text, language, create_file=False)

    # Assert that the output is bytes (image data)
    assert isinstance(image_data, bytes)


def test_create_wordcloud_with_saving():
    # Test create_wordcloud with create_file=True
    text = "This is another sample text for testing the saving functionality."
    language = "en"
    filename = "test_wordcloud.png"

    # Remove the file if it already exists to avoid conflicts
    if os.path.exists(filename):
        os.remove(filename)

    # Create the word cloud and save it as a file
    saved_filename = create_wordcloud(
        text, language, create_file=True, filename=filename
    )

    # Assert that the output is the filename of the saved word cloud
    assert isinstance(saved_filename, str)
    assert os.path.exists(saved_filename)

    # Clean up by removing the saved file
    os.remove(saved_filename)
