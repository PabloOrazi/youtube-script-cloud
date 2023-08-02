[![Test with Python 3.9](https://github.com/PabloOrazi/youtube-script-cloud/actions/workflows/main.yml/badge.svg)](https://github.com/PabloOrazi/youtube-script-cloud/actions/workflows/main.yml)
# youtube-script-cloud

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

2.  Run `make install` in Linux. In Windows, if Make is not installed, 	`pip install --upgrade pip` and	`pip install -r requirements.txt`

3.  Run `python app.py`


## To build and run in Docker 

1.  In Linux, you can run `make install` to build the image. In Windows:

```bash
docker build -t my-flask-app .
```

2.  Run `make run-daemon` to run the container. In Windows:

```bash
docker run -d -p 5000:5000 my-flask-app
```

