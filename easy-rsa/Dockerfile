# base image

FROM ubuntu:latest

# update and install tools
RUN apt update && apt -y upgrade
RUN apt-get update && apt-get install  -y nginx
RUN apt-get update && apt-get install -y python python-pip 
RUN apt-get update && apt-get install -y net-tools
RUN apt-get update && apt-get -y install systemd
RUN apt-get update && apt-get install -y procps
RUN apt-get update && apt-get install -y sudo

# create directory
RUN mkdir -p /home/easy-rsa
COPY . /home/easy-rsa

# remove default configurations from nginx

RUN rm -rf /etc/nginx/sites-enabled
RUN rm -rf /etc/nginx/sites-available
RUN rm -rf /etc/nginx/modules-available

# copy my cofiguration to nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY data /etc/nginx/data

# expose port used
EXPOSE 55000

RUN useradd -s /bin/bash ctfuser 

#USER ctfuser

CMD "/bin/bash" "/home/easy-rsa/start.sh"

