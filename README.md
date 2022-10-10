# be-challenge
<h3 align="center" id="readme-top">README</h3>

  <p align="center">
    be-challenge project!
    <br />
    <a href="https://github.com/stitouN/be-challenge.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/stitouN/be-challenge.git">View Demo (in heroku)</a>
    ·
    <a href="https://github.com/stitouN/be-challenge.git/issues">Report Bug</a>
    ·
    <a href="https://github.com/stitouN/be-challenge.git/issues">Request Feature</a>
  </p>
</div>







<!-- ABOUT THE PROJECT -->
## About The Project

[be-challenge project]

### Problem Statement
Develop an API endpoint to get a list of users.

### Requirements to DB
DB have 1MM records.

### Requirements to API
Pagination support

Filtration support

Cache-Control (client and server-side)


### Built With

* Docker
* Flask-like framework
* PostgreSQL
* GIT
* Swagger-ui
* Redis

### Installation
1-After cloning the project
* Add a file .env on the root of the project and paste this configuration:

```
# postgres conf
POSTGRES_USER=beUser
POSTGRES_PASSWORD=password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=beDb


# cache conf
CACHE_TYPE=redis
CACHE_REDIS_HOST=redis
CACHE_REDIS_PORT=6379
CACHE_REDIS_DB=0
CACHE_REDIS_URL=redis://redis:6379/0
CACHE_DEFAULT_TIMEOUT=500

```

2- Build the project and build the docker images
```http
run docker-compose up --build -d 
```

3- you can access to the API documentation by using this url: 
```http
http://localhost:8000/api/docs
```
4- the result should be like the image below:

![image](https://user-images.githubusercontent.com/7559673/194884147-36ab8cb8-751a-4806-b429-e47d557086a1.png)

Responses for api call:
##Pagination
![image](https://user-images.githubusercontent.com/7559673/194884420-74a2cf5b-a35e-4f2b-bbcb-5d4f16008f71.png)

##Filtration
![image](https://user-images.githubusercontent.com/7559673/194885401-8de91b4d-535f-4590-9dcd-094a38cfef49.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

