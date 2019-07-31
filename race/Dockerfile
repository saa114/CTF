# Get Ubunut configurations
FROM ubuntu

# Get python configurations
FROM python:2.7.11

# Update
#RUN apt-get -y  update 

# Create a directory in docker container
RUN mkdir -p /home/race

# Copy continents from current directory to docker directory
COPY . /home/race

#Open port in docker(must be same port in server)
EXPOSE 19999

#Adds user with non-root permission
RUN useradd -s /bin/bash ctfuser

#Allows user to execute cmd
USER ctfuser

RUN -p 4000:19999
# Execute Program(s)
CMD   "python" /home/race/server.py 


# Note: "python" us used to disregard flags.
