FROM python:3.11

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install -r ./requirements.txt
RUN apt-get install libmagic1

