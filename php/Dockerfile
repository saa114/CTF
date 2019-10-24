FROM ubuntu:16.04

ARG DEBIAN_FRONTEND=noninteractive

# update and install tools
RUN apt update && apt -y upgrade
RUN apt-get update && apt-get install -y python python-pip
RUN apt-get update && apt-get install -y net-tools
RUN apt-get update && apt-get install -y procps
RUN apt-get update && apt-get install -y sudo
RUN apt-get update && apt-get install -y  php7.0-fpm php7.0-mysql
RUN apt-get update && apt-get install  -y nginx


RUN mkdir -p /home/php
COPY . /home/php

RUN mkdir -p /srv/http

#NGINX CONFIGURATION
RUN rm -rf /etc/nginx/sites-enabled
RUN rm -rf /etc/nginx/sites-available
RUN rm -rf /etc/nginx/modules-available
RUN rm -f /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/sites-available /etc/nginx/sites-enabled
RUN chmod 755 /etc/nginx/sites-available /etc/nginx/sites-enabled
COPY nginx.conf /etc/nginx

RUN groupadd site1
RUN useradd -g site1 site1

#PHP CONFIGURATION
RUN rm -f /etc/php/7.0/fpm/pool.d/www.conf
COPY site1.conf /etc/php/7.0/fpm/pool.d
RUN rm -f /etc/php/7.0/fpm/php.ini 
COPY php.ini /etc/php/7.0/fpm
COPY 10-opcache.ini /etc/php/7.0/fpm/conf.d 


#SITE1 CONFIGURATION 
COPY site1 /etc/nginx/sites-available
RUN chown -R nobody:site1 /etc/nginx/sites-available/site1
RUN ln -s /etc/nginx/sites-available/site1 /etc/nginx/sites-enabled/site1
RUN chown -R nobody:site1 /etc/nginx/sites-enabled/site1
RUN chmod 711 /srv/http
RUN mkdir /srv/http/site1
ADD data /srv/http/site1/data
RUN chown -R nobody:site1 /srv/http/site1
RUN chmod 011 /srv/http/site1
RUN chmod 011 /srv/http/site1/*
RUN chmod 044 /srv/http/site1/data/*

EXPOSE 10800

RUN useradd -s /bin/bash ctfuser

#USER ctfuser

CMD  "/bin/bash" "/home/php/start.sh"


