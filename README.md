# CTF problem The Race setup

Step 1) Copy files in local directory

     $git clone https://github.com/saa114/race.git

Step 2) Make an account in docker 
       
     https://www.docker.com/

Step 3) Go to local directory where the github files are.

     $docker login
     
  #Then type user name and password

Step 4) Build docker container

     $docker build -t <docker_username>/<name_your_container> .

Example: docker build -t saa114/race . 

NOTE: Do not forget the dot(.) at the end

Step 4) Run docker application 
  
  #To run application in interactive mode
     
     $docker run -it --rm -p 4000:19999 saa114/race
  Note: The port on the left can be random
  Note: The port on the right must match the port 
        in the server and Dockerfile.
      
  #To run application constantly on port.

     $docker run --rm -p 4000:19999 saa114/race
   
Step 5) To connect to the server

     $curl localhost:4000

      
Step 6) To kill a process running constantly on port

  #First get container ID.
  
     $docker ps
  
  #Then kill the Process.
  
     $docker kill <container_id>
     
Step 7) To push your container to docker hub

     $docker push saa114/race
