# VENV

```
python3 -m venv venv
. venv/bin/activate
```

# INSTALL Flask
`pip install Flask`


# RUN Flask
## Directly, using werkzeug WSGI
`flask --app app run`
or
`flask run`
or 
`flask run --host=127.0.0.1 --port=5000 --debugger`
or (if dnsmasq is on)
`flask run --host=adi-dogar.com --port=5000 --debugger`

## Via Docker
https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/


https://flask.palletsprojects.com/en/2.2.x/quickstart/

% curl 127.0.0.1:5000          # Matches the first rule
You want path:  
% curl 127.0.0.1:5000/foo/bar  # Matches the second rule
You want path: foo/bar


docker exec -it 6af68a02856e uvicorn app.main:app --reload