# encoding: utf-8
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/return_transcript', methods=['POST'])
def login():
    record = json.loads(request.data)
    print(record)
    return "Hello"

# if __name__ == "__main__":
