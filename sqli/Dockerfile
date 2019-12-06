FROM ubuntu:16.04

ARG DEBIAN_FRONTEND=noninteractive

# UPDATE AND INSTALL TOOLS
RUN apt-get update && apt-get install -y  --no-install-recommends \ 
            python python-pip sudo php7.0-fpm php7.0-mysql \
            nginx software-properties-common \
            --no-install-recommends \
            && add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe' \ 
            && apt-get update && apt-get install -y  mysql-server-5.6 \
            --no-install-recommends \
            && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/sqli /srv/http
COPY . /home/sqli

#REMOVE DEFAULT CONFIGURATION
RUN rm -rf /etc/nginx/sites-enabled /etc/nginx/sites-available \
           /etc/nginx/modules-available \
           /etc/nginx/nginx.conf \ 
           /etc/mysql/debian.cnf     
             

RUN mkdir /etc/nginx/sites-available \ 
          /etc/nginx/sites-enabled \ 
          /srv/http/site3 \
          && chmod 755 /etc/nginx/sites-available /etc/nginx/sites-enabled \ 
          && groupadd site3   \
          && useradd -g site3 site3

ADD data /srv/http/site3/data

COPY nginx.conf /etc/nginx 
COPY  my.cnf /etc/mysql/my.cnf 
COPY  debian.cnf /etc/mysql/debian.cnf

#PHP CONFIGURATION
RUN rm -f /etc/php/7.0/fpm/pool.d/www.conf \
          /etc/php/7.0/fpm/php.ini

COPY site3.conf /etc/php/7.0/fpm/pool.d 
COPY php.ini /etc/php/7.0/fpm 
COPY  10-opcache.ini /etc/php/7.0/fpm/conf.d 


#SITE3 CONFIGURATION 
COPY site3 /etc/nginx/sites-available
RUN chown -R nobody:site3 /etc/nginx/sites-available/site3 \
    && ln -s /etc/nginx/sites-available/site3 /etc/nginx/sites-enabled/site3 \
    &&  chown -R nobody:site3 /etc/nginx/sites-enabled/site3 \
    && chmod 711 /srv/http \
    && chown -R nobody:site3 /srv/http/site3 \
    && chown root:root /etc/mysql/debian.cnf \
    && chmod 400 /etc/mysql/debian.cnf \
    && chmod 011 /srv/http/site3  /srv/http/site3/* \
    && chmod 044 /srv/http/site3/data/*


EXPOSE 10811

RUN useradd -s /bin/bash ctfuser

CMD  "/bin/bash" "/home/sqli/start.sh"


