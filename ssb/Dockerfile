FROM 32bit/ubuntu:16.04


COPY source.list /etc/apt/source.list

# update and install tools

#RUN apt update && apt -y upgrade

RUN apt update && apt-get install  -y nginx \
    python python-pip \
    sudo \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# create directory
RUN mkdir -p /home/ssb

COPY . /home/ssb
COPY flag.txt /

RUN rm -rf /etc/nginx/sites-enabled \ 
           /etc/nginx/sites-available \
	   /etc/nginx/modules-available

COPY nginx.conf /etc/nginx/nginx.conf
COPY data /etc/nginx/data

EXPOSE 13131
EXPOSE 64000

RUN useradd -s /bin/bash ctfuser

CMD "/bin/bash" "/home/ssb/start.sh"


