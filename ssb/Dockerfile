FROM yukoff/alpine-32bit
 
# update and install tools    #--arch x86

RUN apk update && apk add --no-cache --upgrade nginx \
    python2 \
    openrc \
    libc6-compat \ 
    sudo \
    bash \
    && rm -rf /var/lib/cache/apk/*

# create directory
RUN mkdir -p /home/ssb \
             /run/nignx

COPY . /home/ssb
COPY flag.txt /

RUN rm -rf /etc/nginx/sites-enabled \ 
           /etc/nginx/sites-available \
	   /etc/nginx/modules-available \
        && chmod 777 /home/ssb/overflow

COPY nginx.conf /etc/nginx/nginx.conf
COPY data /etc/nginx/data

EXPOSE 13131
EXPOSE 64000


RUN addgroup -S ctfgroup && adduser -S ctfuser -G ctfgroup

CMD "/bin/bash" "/home/ssb/start.sh" 




