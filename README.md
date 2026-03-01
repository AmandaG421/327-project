<<<<<<< Updated upstream
This project is introducing us to Docker containers, this inludes running a python based container, deploying a Nginx web server using the docker and then modyfying the Nginx server. We will also need to make multiclient servers; in ur case, we have one server and two clients.
=======
>>>>>>> Stashed changes

## Running it 
- Must have Docker installed on your system 

First clone the repository and navigate to your project directory

command to build the docker image:

 docker build -t my-python-app . 
 
Run the container using the command:

docker run-my-python-app  

## Running the Nginx web server 

Pull from the latest Nginx image using the command:

docker pull nginx:latest 

Run the container: 

docker run -d -p 8080:80 --name my-nginx nginx:latest

Now open http://localhost:8080 in your browser and you should see the default Nginx page 

## Modifying the web server 

Change the directory from default to your local HTML file 

If running on powershell, use this command:

docker run -d -p 8081:80 -v ${PWD}/index.html:/usr/share/nginx/html/index.html nginx:latest

PWD changes the directory
When running another host container, make sure it is ran on a different port that not in use (Ex. change 8080 to 8081) 


## Multi-Client Server container 

To run the yml file use the command:

docker compose up --build

## Troubleshooting 
Commands for debugging: 

docker logs <container_id> 
docker ps 
docker exec-it <container-id> sh

<<<<<<< Updated upstream
docker compose up --build
=======
>>>>>>> Stashed changes
