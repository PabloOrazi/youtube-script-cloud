import click
import os
from click.testing import CliRunner
from yt_transcript_cli import get_script, wordcloud


def test_get_script_with_default_language():
    # Test get_script with default language
    runner = CliRunner()
    result = runner.invoke(get_script, ["https://www.youtube.com/watch?v=OJDkPz3nPjM"])
    assert result.exit_code == 0
    assert "Language:" in result.output
    assert "Downloaded Text:" in result.output


def test_get_script_with_specified_language():
    # Test get_script with specified language
    runner = CliRunner()
    result = runner.invoke(get_script, ["https://www.youtube.com/watch?v=OJDkPz3nPjM", "--language", "en"])
    assert result.exit_code == 0
    assert "Language: en" in result.output
    assert "Downloaded Text:" in result.output


def test_get_script_with_output_file():
    # Test get_script with output file
    runner = CliRunner()
    output_file = "test_output.txt"
    result = runner.invoke(get_script, ["https://www.youtube.com/watch?v=OJDkPz3nPjM", "--output-file", output_file])
    assert result.exit_code == 0
    assert "Language:" in result.output
    assert not result.output.endswith("Downloaded Text: \n")

    # Clean up by removing the created file
    if output_file:
        try:
            os.remove(output_file)
        except OSError:
            pass


def test_wordcloud():
    # Test wordcloud function
    runner = CliRunner()
    result = runner.invoke(wordcloud, ["https://www.youtube.com/watch?v=OJDkPz3nPjM"])
    assert result.exit_code == 0

    # Clean up by removing the created file
    output_file = "wordcloud.png"
    if os.path.exists(output_file):
        os.remove(output_file)
