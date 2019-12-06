# Get latest ubuntu image
FROM ubuntu

# Get python configurations
RUN apt update && apt -y upgrade \
    python python-pip \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Update
#RUN apt-get -y  update 

# Create a directory in docker container
RUN mkdir -p /home/race

# Copy continents from current local directory to docker directory
COPY . /home/race

#Open port in docker(must be same port in server)
EXPOSE 19999

#Adds user with non-root permission
RUN useradd -s /bin/bash ctfuser

#Allows user to execute cmd
USER ctfuser

# Execute Program(s)
CMD   "python" /home/race/question.py && "python" /home/race/server.py 


# Note: "python" us used to disregard flags.
