# encoding: utf-8
from flask import Flask, request, jsonify, render_template,send_file
import json

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/return_transcript', methods=['POST'])
def post_request():
    # print(request)
    # print(request.data)        
    record = json.loads(request.data)
    # print(record)

    # TODO : get video title
    video_title = "Video Title"
 
    # Generate or manipulate the image
    image = generate_image()

    # Convert the image to base64 string
    buffered = BytesIO()
    image.save(buffered, format='JPEG')
    encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    # return send_file('photo-1481349518771-20055b2a7b24.jfif', mimetype='image/jpeg')

    response = {
        'image': encoded_image,
        "video_title" : video_title,
        'url': record["inputYouTubeUrl"]
    }

    return jsonify(response)



from io import BytesIO
from PIL import Image
import base64

def generate_image():
    # Generate or manipulate the image using PIL or any other library
    image = Image.new('RGB', (200, 200), color='red')
    return image

if __name__ == "__main__":
    app.run(debug=True)