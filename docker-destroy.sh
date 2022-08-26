#!/bib/bash

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker container prune -f
docker image prune -f
docker volume prune -f
docker network prune -f