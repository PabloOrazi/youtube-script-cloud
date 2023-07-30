FROM python:3
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python models_setup.py

COPY . .
CMD flask run
# ENTRYPOINT ["flask", "run", "--app", "app", "--host=0.0.0.0"]