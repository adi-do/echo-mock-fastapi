# ECHO API

Very simple and straight forward API for ECHO purposes. When a request is sent to this API, it will simply return back to the client all request information packed in a JSON object.

Of course, you can use the API for playground purposes also. You just have to add new routes to the `main.py` file with some logic to build a useful response.

## API Usage

By sending a request to "/" you will get in return a simple "Hello World" message.

By sending a request to "/echo" followed by any other (series of) path and query parameters and having any body and header desired, you will have a complete JSON as a response, containing all the data received by the API server. In other words, it will give you a full picture of what your client application is sending to the server.

## API Documentation

In your browser, go to http://localhost:8000/docs to see the API documentation (swagger).

## INSTALL

based on https://fastapi.tiangolo.com/

# Requisites
- Python 3.8

### RUN locally (dev)

1. Create virtual env
    git clone git@github.com:adi-do/echo-mock-fastapi.git
    cd ./echo-mock-fastapi
    python -m venv echo-api-venv
    . echo-api-venv/bin/activate

2. Install requirements
    pip install -r requirements.txt

3. RUN via ASGI
    echo-api-venv/bin/uvicorn app.main:app
    => Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

### RUN via Docker
    docker build -t echo-mock-fastapi .
    docker run -d --name echo-mock-fastapi -p 8000:80 echo-mock-fastapi

### RUN via Docker Compose
    docker-compose up -d --build

#### Install packages inside docker (with docker-compose)
- Install the package locally and add it to the requirements.txt file
- Run `docker-compose down` to stop the container
- Run `docker-compose up -d --build` to rebuild the image. The Dockerfile will install the new package
