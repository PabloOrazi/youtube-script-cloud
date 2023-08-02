import click
from functions import extract_id, download_script, create_wordcloud


@click.group()
def cli():
    pass


@cli.command()
@click.argument("url")
@click.option(
    "--language", "-l", default=None, help="Language to download the video transcript in"
)
@click.option(
    "--output-file", "-o", default=None, help="Save the YouTube transcript to a file"
)
@click.option(
    "--joined-script",
    "-j",
    default=True,
    help="Join text with True, raw with timestamps False",
)
def get_script(url, language, output_file, joined_script):
    """
    Download a YouTube video transcript by its URL.

    Example:
        python yt_transcript_cli.py get-script https://www.youtube.com/watch?v=OJDkPz3nPjM --language en --output-file script.txt --joined-script false
    """    
    video_id = extract_id(url)
    language, text = download_script(video_id, language, joined_script)
    click.echo(f"Language: {language}")
    if output_file is None:
        click.echo(f"Downloaded Text: \n{text}")
    else:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(str(text))
        click.echo(f"Downloaded text in file {output_file}")


@cli.command()
@click.argument("url")
@click.option("--language", default=None, help="Language of the script")
@click.option(
    "--output-file", "-o", default="wordcloud.png", help="Save the word cloud to a file"
)
def wordcloud(url, language, output_file):
    """
    Generate a word cloud from the transcript of a YouTube video specified by its URL.

    Example:
        python yt_transcript_cli.py get-script OJDkPz3nPjM --language en --output-file wordcloud.png
    """    
    video_id = extract_id(url)
    language, text = download_script(video_id, language)
    create_wordcloud(text, language, create_file=True, filename=output_file)


if __name__ == "__main__":
    cli()
