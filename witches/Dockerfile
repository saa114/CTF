FROM ubuntu

FROM python:2.7.11

RUN mkdir /home/witcher

COPY . /home/witcher

RUN useradd -s /bin/bash ctfuser

USER ctfuser

CMD "python" /home/witcher/question.py

