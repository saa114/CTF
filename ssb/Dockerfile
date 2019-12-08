FROM yukoff/alpine-32bit


#COPY source.list /etc/apt/source.list

# update and install tools

#RUN apt update && apt -y upgrade

RUN apk update && apk add --no-cache --upgrade --arch x86 nginx \
    python2 \
    libc6-compat \ 
    sudo \
    bash \
    && rm -rf /var/lib/cache/apk/*

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

RUN addgroup -S ctfgroup && adduser -S ctfuser -G ctfgroup

CMD "/bin/bash" "/home/ssb/start.sh"


