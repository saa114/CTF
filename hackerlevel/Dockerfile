FROM ubuntu:latest

# update and install tools
RUN apt update && apt -y upgrade \
    && apt-get install  -y python python-pip \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*


# create directory
RUN mkdir -p /home/hackerlevel
COPY . /home/hackerlevel

EXPOSE 11111

RUN useradd -s /bin/bash ctfuser

USER ctfuser

CMD  "python" "/home/hackerlevel/flag_question.py" && "python" "/home/hackerlevel/server.py"


