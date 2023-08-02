[![Test with Python 3.9](https://github.com/PabloOrazi/youtube-script-cloud/actions/workflows/main.yml/badge.svg)](https://github.com/PabloOrazi/youtube-script-cloud/actions/workflows/main.yml)
# youtube-script-cloud

This is a Flask app where you input a YouTube video link and it makes a wordcloud out of the transcript of the video.

![image](https://github.com/PabloOrazi/youtube-script-cloud/assets/15095885/2b70cb65-f9e0-40e1-8de9-a780ab8e4c15)

There is also a Command Line Interface (CLI) that you can call to get the transcript

```bash
python yt_transcript_cli.py get-script https://www.youtube.com/watch?v=ucP-Gh-wS9E --language en --output-file script.txt
```

and to make a wordcloud and save it into a file:

```bash
python yt_transcript_cli.py get-script OJDkPz3nPjM --language en --output-file wordcloud.png
```



## To run it locally follow these steps 

1.  Create virtual environment and source

    In Linux:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    In Windows

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

2. Clone this repo 

    ```bash
    git clone https://github.com/PabloOrazi/youtube-script-cloud.git
    ```

3.  Run `make install` in Linux. In Windows, if Make is not installed, 	`pip install --upgrade pip`,	`pip install -r requirements.txt` and `python models_setup.py`

To run the Flask App

4.  Run `python app.py`

5.  Go to url http://127.0.0.1:5000 in your favorite Web Browser 

To run the CLI

4.  Run `python yt_transcript_cli.py get-script https://www.youtube.com/watch?v=ucP-Gh-wS9E --language en --output-file script.txt` to get the transcript into "script.txt"


## To build and run in Docker 

1.  In Linux, you can run `make install` to build the image. In Windows:

    ```bash
    docker build -t my-flask-app .
    ```

2.  Run `make run-daemon` to run the container. In Windows:

    ```bash
    docker run -d -p 5000:5000 my-flask-app
    ```

3.  Go to url http://127.0.0.1:5000 in your favorite Web Browser 
