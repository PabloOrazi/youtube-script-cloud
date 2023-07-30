# encoding: utf-8
from flask import Flask, request, jsonify, render_template,send_file
from urllib.parse import urlparse, parse_qs
from functions import download_script, create_wordcloud
import json
import base64

app = Flask(__name__)

# @app.route("/hello")
# def hello_world():
#     return "<p>Hello World!</p>"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/return_transcript', methods=['POST'])
def post_request():
    # print(request)
    # print(request.data)        
    record = json.loads(request.data)
    link = record["inputYouTubeUrl"]
    # print(record)
    video_id = parse_qs(urlparse(link).query)["v"][0]
    
    video_title = "Word Cloud"
 
    # Generate or manipulate the image
    debug=False
    if not debug:
        language, text = download_script(video_id)
        image_data = create_wordcloud(text,
                                    language)
        encoded_image = base64.b64encode(image_data).decode('utf-8')
    else:
        image = generate_image()
        # Convert the image to base64 string
        buffered = BytesIO()
        image.save(buffered, format='JPEG')
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    response = {
        'image': encoded_image,
        "video_title" : video_title,
        'url': record["inputYouTubeUrl"],
        'url_youtube': f"https://www.youtube.com/embed/{video_id}"
    }

    return jsonify(response)



from io import BytesIO
from PIL import Image

def generate_image():
    # Generate or manipulate the image using PIL or any other library
    image = Image.new('RGB', (400, 400), color='red')
    return image

if __name__ == "__main__":
    app.run(debug=True)