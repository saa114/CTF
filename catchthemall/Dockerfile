FROM ubuntu

FROM python:2.7.11

RUN mkdir /home/catchthemall

COPY . /home/catchthemall

RUN useradd -s /bin/bash ctfuser

USER ctfuser

EXPOSE 4000 

CMD "python" /home/catchthemall/server.py
