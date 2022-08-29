My career is a small project carried out to demonstrate my skills and proficiency in some technologies. This is the Python/Javascript (Flask/Vue) version of the project and I am using the following technologies;

## 💻 Technologies and Tools
![](https://img.shields.io/badge/Code-Python-blueviolet?logo=python&logoColor=white) ![](https://img.shields.io/badge/Code-Javascript-blueviolet?logo=javascript&logoColor=white) ![](https://img.shields.io/badge/Code-HTML-blueviolet?logo=html5&logoColor=white) ![](https://img.shields.io/badge/Code-CSS-blueviolet?logo=html5&logoColor=white) ![](https://img.shields.io/badge/Code-Flask-blueviolet?logo=python&logoColor=white) ![](https://img.shields.io/badge/Code-Jinja-blueviolet?logo=jinja&logoColor=white) ![](https://img.shields.io/badge/Code-VueJS-blueviolet?logo=Javascript&logoColor=white) ![](https://img.shields.io/badge/Code-SQLAlchemy-blueviolet?logo=python&logoColor=white) ![](https://img.shields.io/badge/Code-FastAPI-blueviolet?logo=python&logoColor=white) ![](https://img.shields.io/badge/Code-Docker-blueviolet?logo=docker&logoColor=white) ![](https://img.shields.io/badge/Code-DockerCompose-blueviolet?logo=python&logoColor=white) ![](https://img.shields.io/badge/Code-UnitTest-blueviolet?logo=docker&logoColor=white) ![](https://img.shields.io/badge/Code-Pytest-blueviolet?logo=python&logoColor=white)

## How to run? Docker Compose
In the 'app' folder we have a simple list registration application written using Flask (python), Jinja as a framework and using VueJs (Javascript) on the frontend. We just need to run these commands at the project root folder

```sh
docker-compose build #build the containers
docker-compose up -d #run the containers
```
It will up the following services:
- ``db:`` A Postgres Database will be available at the http://localhost:54321 
- ``api:`` A Fastapi instance will be available at the http://localhost:5100/jobs 
- ``app:`` A Flask App (With VueJS Frontend) instance will be available at the http://localhost:5200
- ``admin:`` A PGAdmin (Python/Postgres) instance will be available at the http://localhost:5300

## Continuos Integration/Delivery (CD/CI)
- ``Circle CI:`` This repository is integrated trough the Circle CI solution
- 

## Contacts
![](https://img.shields.io/badge/LinkedIn-alexandreconrado-blue?url=https://www.linkedin.com/in/alexandreconrado/&logo=linkedin&logoColor=white) ![](https://img.shields.io/badge/Gmail-xandee1977@gmail.com-red?logo=gmail&logoColor=white)