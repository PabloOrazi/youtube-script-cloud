FROM python:3.10
# FROM python:3.10-alpine
# RUN apk update
# RUN apk add --no-cache gcc musl-dev g++

WORKDIR /app
COPY requirements.txt ./

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN python -m venv venv
# RUN source venv/bin/activate
# RUN venv/bin/pip install --upgrade pip setuptools 
# RUN venv/bin/pip install --no-cache-dir -r requirements.txt


RUN python models_setup.py

EXPOSE 5000
CMD flask run --host 0.0.0.0 --port 5000