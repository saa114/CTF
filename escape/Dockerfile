# base image

FROM ubuntu:latest

# update and install tools
RUN apt update && apt -y upgrade \
    && apt-get install  -y python python-pip \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*


# create directory
RUN mkdir -p /home/escape
COPY . /home/escape
COPY flag.txt /

# expose port used
EXPOSE 17777

RUN useradd -s /bin/bash ctfuser 

USER ctfuser

CMD python "/home/escape/question.py" && python "/home/escape/server.py"

