from typing import Union

from fastapi import FastAPI, Request, Body
from fastapi.logger import logger
import re


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "FastAPI Developer"}

echo_basepath = "/echo"

def reply_echo(request: Request, req_body = None):
    hostname = re.sub("(https?:\/\/)|(:\d{2,4})", '', request.base_url._url).split('/')[0]
    port     = re.search(r"(:\d{2,4})", request.base_url._url).group().split(":")[1]
    schema   = request.base_url._url.split("://")[0]
    response = {
        "author": "Adrian Ruben Dogar",
        "client": request.client,
        "method": request.method,
        "url": request.url._url,
        "schema": schema,
        "endpoint": request.base_url._url,
        "hostname": hostname,
        "basepath": echo_basepath,
        "port": port,
        "path-params": request.path_params,
        "query-params": request.query_params,
        "headers": request.headers,
        "body": req_body,
        "cookies": request._cookies,
        "dir": dir(request),
    }

    return response

@app.get(echo_basepath + "{resource:path}")
def reply_get(request: Request):
    response = reply_echo(request)
    return response

@app.post(echo_basepath + "{resource:path}")
async def reply_post(request: Request):
    # TODO : Handle all other different bodies (XML, www-form + url-encoded, file content, etc.)
    # TODO : Handle gzip decoding
    # TODO : Handle the exception if no body was sent
    req_body = await request.json()
    response = reply_echo(request, req_body)
    return response

""" def reply_echo(resource: str, q: Union[str, None] = None):
    response = {
        "author": "Adrian Ruben Dogar",
        "basepath": "/echo",
        "path": "/" + resource,
        "query-params": q
    }
    return response
 """