Step 1) Copy files in local directory
# In your local directory

     $git clone https://github.com/saa114/race.git

Step 2) Make an account in docker 

Step 3) Go to local directory

Step 4) Build docker application

     $docker build -t <docker_username>/<name_your_container> .

Example: docker build -t saa114/race . 
Note: DO NOT FORGET THE DOT(.) AT THE END

Step 4) Run docker application 
  
  #To run application in interactive mode
     
     $docker run -it --rm -p 4000:19999 saa114/race

  #To run application constantly on port.

     $docker run --rm -p 4000:19999 saa114/race
Step 5) To connect to the server

     $curl localhost:4000

      

