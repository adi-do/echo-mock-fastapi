based on https://github.com/patrickloeber/python-docker-tutorial

# USE venv
    cd ~/code/echo-mock-fastapi
    python3 -m venv venv
    . venv/bin/activate

# INSTALL FastAPI
    pip install fastapi uvicorn

# FETCH the requirements
    cd ~/code/echo-mock-fastapi/app
    pip3 freeze > requirements.txt

# RUN via ASGI
    uvicorn app.main:app
    => Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

# RUN via Docker
    docker build -t echo-mock-fastapi .
    docker run -d --name echo-mock-fastapi -p 8000:80 echo-mock-fastapi

# RUN via Docker Compose
    docker-compose up -d --build

# Install packages inside docker (with docker-compose)
- Install the package locally and add it to the requirements.txt file
- Run `docker-compose down` to stop the container
- Run `docker-compose up -d --build` to rebuild the image. The Dockerfile will install the new package
