FROM ubuntu:latest

RUN apt update && apt -y upgrade \
    && apt-get install -y python python-pip \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /home/witcher

COPY . /home/witcher

RUN useradd -s /bin/bash ctfuser

USER ctfuser

CMD "python" /home/witcher/question.py

