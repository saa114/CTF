# base image

FROM ubuntu:latest

# update and install tools
RUN apt update && apt -y upgrade \
    && apt-get install  -y nginx \
    python python-pip \
    sudo \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# create directory
RUN mkdir -p /home/caesar
COPY . /home/caesar 

# remove default configurations from nginx

RUN rm -rf /etc/nginx/sites-enabled \
           /etc/nginx/sites-available \
	   /etc/nginx/modules-available

# copy my cofiguration to nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY data /etc/nginx/data

# expose port used
EXPOSE 45000

RUN useradd -s /bin/bash ctfuser 

#USER ctfuser

CMD "/bin/bash" "/home/caesar/start.sh"

