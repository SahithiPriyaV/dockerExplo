
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