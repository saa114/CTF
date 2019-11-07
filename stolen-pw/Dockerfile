# base image

FROM ubuntu:latest

# update and install tools
RUN apt update && apt -y upgrade
RUN apt-get update && apt-get install -y python python-pip 
RUN apt-get update && apt-get install -y net-tools
RUN apt-get update && apt-get -y install systemd
RUN apt-get update && apt-get install -y procps
RUN apt-get update && apt-get install -y sudo

# create directory
RUN mkdir -p /home/stolen-pw
COPY . /home/stolen-pw

# expose port used
EXPOSE 20202

RUN useradd -s /bin/bash ctfuser 

USER ctfuser

CMD python "/home/stolen-pw/question.py" && python "/home/stolen-pw/server.py"

