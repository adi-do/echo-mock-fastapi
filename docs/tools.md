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

# RUN ASGI
    uvicorn app.main:app
    => Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

docker build -t echo-mock-fastapi .

docker run -d --name echo-mock-fastapi -p 8000:80 echo-mock-fastapi 