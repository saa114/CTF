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
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'
RUN apt-get update && apt-get install -y mysql-server-5.6



RUN mkdir -p /home/sqli
COPY . /home/sqli

RUN mkdir -p /srv/http

#NGINX CONFIGURATION
RUN rm -rf /etc/nginx/sites-enabled
RUN rm -rf /etc/nginx/sites-available
RUN rm -rf /etc/nginx/modules-available
RUN rm -f /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/sites-available /etc/nginx/sites-enabled
RUN chmod 755 /etc/nginx/sites-available /etc/nginx/sites-enabled
COPY nginx.conf /etc/nginx

RUN groupadd site3
RUN useradd -g site3 site3

#PHP CONFIGURATION
RUN rm -f /etc/php/7.0/fpm/pool.d/www.conf
COPY site3.conf /etc/php/7.0/fpm/pool.d
RUN rm -f /etc/php/7.0/fpm/php.ini 
COPY php.ini /etc/php/7.0/fpm
COPY 10-opcache.ini /etc/php/7.0/fpm/conf.d 


#SITE3 CONFIGURATION 
COPY site3 /etc/nginx/sites-available
RUN chown -R nobody:site3 /etc/nginx/sites-available/site3
RUN ln -s /etc/nginx/sites-available/site3 /etc/nginx/sites-enabled/site3
RUN chown -R nobody:site3 /etc/nginx/sites-enabled/site3
RUN chmod 711 /srv/http

RUN mkdir /srv/http/site3
ADD data /srv/http/site3/data
RUN chown -R nobody:site3 /srv/http/site3
RUN chmod 011 /srv/http/site3
RUN chmod 011 /srv/http/site3/*
RUN chmod 044 /srv/http/site3/data/*

#RUN rm -rf /var/lib/mysql
COPY my.cnf /etc/mysql/my.cnf
RUN rm -f /etc/mysql/debian.cnf
COPY debian.cnf /etc/mysql/debian.cnf
RUN chown root:root /etc/mysql/debian.cnf
RUN chmod 400 /etc/mysql/debian.cnf

#RUN rm  -f /etc/mysql/my.cnf
#COPY debian.cnf /etc/mysql/my.cnf

#RUN service mysql start
#RUN mysql -u debian-sys-maint -pKkwb9qPUK4Ou7OAY -e 'source  /home/sqli/mysql-alldbs.sql'


EXPOSE 10811

RUN useradd -s /bin/bash ctfuser

#USER ctfuser

CMD  "/bin/bash" "/home/sqli/start.sh"


