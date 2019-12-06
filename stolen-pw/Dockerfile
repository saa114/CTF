# base image

FROM ubuntu:latest

# update and install tools
RUN apt update && apt -y upgrade \
    && apt-get install  -y python python-pip \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# create directory
RUN mkdir -p /home/stolen-pw
COPY . /home/stolen-pw

# expose port used
EXPOSE 20202

RUN useradd -s /bin/bash ctfuser 

USER ctfuser

CMD  python "/home/stolen-pw/question.py" && python "/home/stolen-pw/server.py"


