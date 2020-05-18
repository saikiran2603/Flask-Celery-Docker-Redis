FROM python:3.8-slim

# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

#COPY app.py /app.py
ADD . /module_worker
WORKDIR /module_worker

ENTRYPOINT celery -A module worker --loglevel=info -Q module -c 5
