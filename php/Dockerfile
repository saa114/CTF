FROM ubuntu:16.04

#Makes tools avoid asking questions when downloading.
ARG DEBIAN_FRONTEND=noninteractive

# update and install tools
RUN apt-get update && apt-get install -y \
            python python-pip sudo php7.0-fpm php7.0-mysql \
            nginx software-properties-common \
            --no-install-recommends \
            && rm -rf /var/lib/apt/lists/*

#Create a directory
RUN mkdir -p /home/php \
             /srv/http \
             /srv/http/site1

COPY . /home/php

#Change Nginx Configurations
RUN rm -rf /etc/nginx/sites-enabled \
           /etc/nginx/sites-available \
          /etc/nginx/modules-available \
          /etc/php/7.0/fpm/pool.d/www.conf \
          /etc/php/7.0/fpm/php.ini


ADD data /srv/http/site1/data
COPY nginx.conf /etc/nginx

#Create a new user and group
RUN groupadd site1 \
    && useradd -g site1 site1 \
    && useradd -s /bin/bash ctfuser

#PHP CONFIGURATION
COPY site1.conf /etc/php/7.0/fpm/pool.d
COPY php.ini /etc/php/7.0/fpm
COPY 10-opcache.ini /etc/php/7.0/fpm/conf.d 

#Expose port
EXPOSE 10800

CMD  "/bin/bash" "/home/php/start.sh"



