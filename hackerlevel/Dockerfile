FROM ubuntu:latest

# update and install tools
RUN apt update && apt -y upgrade
RUN apt-get update && apt-get install -y python python-pip
RUN apt-get update && apt-get install -y net-tools
RUN apt-get update && apt-get install -y procps
#RUN apt-get update && apt-get install -y gnome-terminal

# create directory
RUN mkdir -p /home/hackerlevel
COPY . /home/hackerlevel

EXPOSE 11111

RUN useradd -s /bin/bash ctfuser

USER ctfuser

CMD "python" "/home/hackerlevel/server.py"

