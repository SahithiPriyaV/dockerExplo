
Create Virtual environment
    conda create -n dockerapp python=3.10
Install dependencies
    pip install flask
To export pip dependencies to yml file
    conda export >requirements.yml
To apply yaml changes to your enviroment
    conda env update -f environment.yml

Python:
3.10


(dockerapp) D:\codeexplo\docker\pythonApp>docker build -t pythonflaskapp .
(dockerapp) D:\codeexplo\docker\pythonApp>docker images  
(dockerapp) D:\codeexplo\docker\pythonApp>docker run -d -p 8000:5000 --name python-cont-1 pythonflaskapp
(dockerapp) D:\codeexplo\docker\pythonApp>docker exec -it python-cont-1 /bin/bash
(dockerapp) D:\codeexplo\docker\pythonApp>docker ps --all    
(dockerapp) D:\codeexplo\docker\pythonApp>ddocker stop 2d1bbde9f0e0      
(dockerapp) D:\codeexplo\docker\pythonApp>docker container prune

Case issue
After making app mount i forgot dbig true in flask so container even changes in detectin container memory not detcting changing in browser, as last service running on flask app without debug 
so stoped and start container
then any changes in file is now refletin at both memory and browser url ping

(dockerapp) D:\codeexplo\docker\pythonApp>for /f %i in ('docker ps -q') do docker stop %i  
to stop all container at once

(dockerapp) D:\codeexplo\docker\pythonApp>docker run -d -p 8001:5000 -v app_code:/app -v app_logs:/logs - name python-cont-6 pythonflaskapp
for named volume


to build docker images from docker compose yml

D:\codeexplo\docker>docker compose -f docker-compose.yml build


to run docker containers
D:\codeexplo\docker>docker compose up -d


to see docker logs

D:\codeexplo\docker>docker compose logs -f


ping not found
root@9d029bc8aa21:/app# apt-get update && apt-get install -y iputils-ping

D:\codeexplo\docker>docker network inspect bridge
t create container in different network
D:\codeexplo\docker>docker network create mybridge
D:\codeexplo\docker>docker run -d --network mybridge -p 8000:5000 --name python-cont-1 pythonflaskapp 
D:\codeexplo\docker>docker network connect --alias postgres-db bridge postgres-db