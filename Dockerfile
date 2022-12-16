FROM debian:11
FROM python:3.10.5-slim-buster

WORKDIR /app.py/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update -y && apt-get upgrade -y 

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3", "-m", "app.py"]
