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
RUN mkdir -p /home/catchthemall
COPY . /home/catchthemall
#COPY rc.local /etc
#RUN chmod +x /etc/rc.local
# remove default configurations from nginx

RUN rm -rf /etc/nginx/sites-enabled
RUN rm -rf /etc/nginx/sites-available
RUN rm -rf /etc/nginx/modules-available

#RUN rm -rf /etc/nginx 

#RUN mkdir -p /etc/nginx

#RUN mkdir -p /var/lib/nginx/body
#RUN service nginx start

# copy my cofiguration to nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY data /etc/nginx/data

#RUN chmod -R go+rwx /var/log/nginx
#RUN chmod -R go+rwx /var/lib/nginx

# expose port used
EXPOSE 65000

#CMD service nginx start
# remove root privileges

#RUN service nginx start
#RUN systemctl start nginx
#RUN /bin/bash /etc/init.d/nginx start


#RUN systemctl start nginx

#RUN update-rc.d nginx defaults
RUN useradd -s /bin/bash ctfuser 

#RUN systemctl start nginx
#RUN systemctl enable nginx
#RUN service nginx start

#USER ctfuser

CMD "/bin/bash" "/home/catchthemall/start.sh"
#CMD service nginx start && sudo -u ctfuser "python" "/home/catchthemall/question.py"

#CMD "nginx" "-g" "daemon off;"
# &&  sudo -u ctfuser "python" "/home/catchthemall/question.py"  
 #"/bin/bash" "/etc/init.d/nginx" "start"  && "python" "/home/catchthemall/question.py"



