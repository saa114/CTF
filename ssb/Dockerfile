FROM ubuntu:latest

# update and install tools
RUN apt update && apt -y upgrade
RUN apt-get update && apt-get install  -y nginx
RUN apt-get update && apt-get install -y python python-pip
RUN apt-get update && apt-get install -y net-tools
RUN apt-get update && apt-get install -y procps
RUN apt-get update && apt-get install -y sudo


# create directory
RUN mkdir -p /home/ssb
COPY . /home/ssb

RUN rm -rf /etc/nginx/sites-enabled
RUN rm -rf /etc/nginx/sites-available
RUN rm -rf /etc/nginx/modules-available

COPY nginx.conf /etc/nginx/nginx.conf
COPY data /etc/nginx/data

EXPOSE 13131
EXPOSE 64000

RUN useradd -s /bin/bash ctfuser

#USER ctfuser

#RUN service nginx start
#CMD service nginx start
CMD "/bin/bash" "/home/ssb/start.sh"


