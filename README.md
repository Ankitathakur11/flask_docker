
# _Dockerizing a Flask application with a MySQL Database_

## Technologies Used

* Python
* docker
* docker-compose

# _Setup/Installation Requirements_

# You can run the code by using any one of the following ways:

## 1.Using docker

- Download or clone the code: https://github.com/ajayjatav777/flask_docker.git
- Install the dependencies.
- build docker image:
	- sudo docker build -t flask-mysql-docker-api -f Dockerfile .
- run docker image:
	- sudo docker run --rm -d --network mysqlnet --name rest-server -p 8000:5000 flask-mysql-docker-api
- configure and run a database in a container by using the following commands:
	- sudo docker volume create mysql
	- sudo docker volume create mysql_config
	- sudo docker network create mysqlnet
	- sudo docker run --rm -d -v mysql:/var/lib/mysql -v mysql_config:/etc/mysql -p 3306:3306 --network mysqlnet --name mysqldb -e MYSQL_ROOT_PASSWORD=p@ssw0rd1 mysql	

- Now you can browse here:
  - http://localhost:8000/dbinit
  - http://localhost:8000/getdata
	
## 2.Using docker-compose

- Download or clone the code: https://github.com/ajayjatav777/flask_docker.git
- Install the dependencies.
- build and run containers:
	- sudo docker-compose -f docker-compose.dev.yml up --build

## 2. Pull our image from the docker hub

- to pull an image write the following command in terminal
	- sudo docker pull webtunixdc/flask-mysql-docker-api:latest
- run docker image:
	- sudo docker run --rm -d --network mysqlnet --name rest-server -p 8000:5000 flask-mysql-docker-api
- configure and run a database in a container by using the following commands:
	- sudo docker volume create mysql
	- sudo docker volume create mysql_config
	- sudo docker network create mysqlnet
	- sudo docker run --rm -d -v mysql:/var/lib/mysql -v mysql_config:/etc/mysql -p 3306:3306 --network mysqlnet --name mysqldb -e MYSQL_ROOT_PASSWORD=p@ssw0rd1 mysql	

- Now you can browse here:
  - http://localhost:8000/dbinit
  - http://localhost:8000/getdata
# _set up a CI/CD pipeline using GitHub Actions_
  - Make a github repository
  - Login docker hub account 
  - Go to the github repository click setting>new repository secret> new secret
  - Create a new secret with the name Docker_hub_username and Docker_ID as value
  - Create a new Personal Access Token (PAT). To create a new token, go to Docker hub setting and then click New access token
  - Now, add this Personal access token as a second secret into the github secrets UI with the name Docker_hub_access_token and give token_value as value
  - Setup the github action workflow
  - Go to your repository in GitHub and then click Actions>New workflow.
  - Make a yml file

	
