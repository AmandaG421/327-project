This project is introducing us to Docker containers, this inludes running a python based container, deploying a Nginx web server using the docker and then modyfying the Nginx server. We will also need to make multiclient servers; in ur case, we have one server and two clients.

## Running it 
- Must have Docker installed on your system 

First clone the repository and navigate to your project directory

Use
 docker build -t my-python-app . 
 
 command to build the docker image 

Run the container using the command 

docker run-my-python-app  

## Running the Nginx web server 

Pull from the latest Nginx image using the command 

docker pull nginx:latest 

Run the container 

docker run -d -p 8080:80 --name my-nginx nginx:latest

Now open http://localhost:8080 in your browser and you should see the default Nginx page 

## Modifying the web server 

Make sure the index.html file is updated


## Multi-Client Server container 

To run the yml file use the command 

docker compose up --build
