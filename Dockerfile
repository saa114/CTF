# Get Ubunut configurations
FROM ubuntu

# Get python configurations
FROM python:2.7.11

# Update
#RUN apt-get -y  update


#RUN  apt-get -y install linux-headers-amd64 build-essential libc-dev gcc

# Create a directory in docker container
RUN mkdir -p /home/race

# Copy continents from current directory to docker directory
COPY . /home/race

EXPOSE 19999

USER 5000
# Execute Program(s)
CMD   "python" /home/race/server.py 


# Note: "echo" is used when to output bash. 
#       "python" us used to disregard flags.
