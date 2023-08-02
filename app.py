# encoding: utf-8
from flask import Flask, request, jsonify, render_template
from functions import download_script, create_wordcloud, extract_id
import json
import base64

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/return_transcript", methods=["POST"])
def post_request():
    # print(request)
    # print(request.data)
    record = json.loads(request.data)
    link = record["inputYouTubeUrl"]
    # print(record)
    video_id = extract_id(link)

    video_title = "Word Cloud"

    # Generate or manipulate the image
    language, text = download_script(video_id)
    image_data = create_wordcloud(text, language)
    encoded_image = base64.b64encode(image_data).decode("utf-8")

    response = {
        "image": encoded_image,
        "video_title": video_title,
        "url": record["inputYouTubeUrl"],
        "url_youtube": f"https://www.youtube.com/embed/{video_id}",
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
