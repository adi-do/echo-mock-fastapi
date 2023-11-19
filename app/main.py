from typing import Union

from fastapi import FastAPI, Request

from fastapi.logger import logger
import re
import json
import xml.etree.ElementTree as ET
import xmljson

from app.Messages import Messages

app = FastAPI()
echo_basepath = "/echo"
messages = Messages()

@app.get("/")
def read_root():
    return {"Hello": "FastAPI Developer"}


@app.get(echo_basepath + "{resource:path}")
def reply_get(request: Request):
    response = reply_echo(request)
    return response
    # TODO add warnings and errors if GET and request_body != None


@app.post(echo_basepath + "{resource:path}")
async def reply_post(request: Request):
    # TODO : Handle all other different bodies (XML, www-form + url-encoded, file content, etc.)
    # TODO : Handle gzip decoding
    # TODO : Handle the exception if no body was sent
    #req_body = await request.json()
    req_body = await request.body()
    response_format = set_response_format(request)
    request_format, parsed_body = parse_request_data(req_body.decode('utf-8'), output_format=response_format)
    response = reply_echo(
        request,
        request_body=parsed_body,
        request_format=request_format,
        response_format=response_format
    )
    return response


############################################################


def reply_echo(
        request: Request,
        request_body=None,
        request_format=None,
        response_format=None
    ):

    # Add warning and error messages if any, to the response payload
    msg = {}
    if len(messages.errors) > 0:
        msg["errors"] = messages.errors
    if len(messages.warnings) > 0:
        msg["warnings"] = messages.warnings

    hostname = re.sub("(https?:\/\/)|(:\d{2,4})", '', request.base_url._url).split('/')[0]
    port = re.search(r"(:\d{2,4})", request.base_url._url).group().split(":")[1]
    schema = request.base_url._url.split("://")[0]

    response = {
        "messages": msg,
        "response_format": response_format,
        "echo": {
            "version": "0.0.1",
            "author": "Adrian Ruben Dogar",
        },
        "client": request.client,
        "method": request.method,
        "url": request.url._url,
        "schema": schema,
        "endpoint": request.base_url._url,
        "hostname": hostname,
        "basepath": echo_basepath,
        "port": port,
        "path-params": request.path_params,
        "query-params": dict(request.query_params),
        "headers": dict(request.headers),
        # TODO return all headers if any is duplicated
        "body": {
            "format": request_format,
            "data": request_body,
        },
        "cookies": request._cookies,
    }

    if response_format == "xml":
        #convert json to xml
        response = ET.fromstring(json.dumps(response))
        response = ET.tostring(response, encoding='utf-8').decode('utf-8')

        #json_data = json.dumps(response)  # Convert response to JSON string
        #xml_data = xmljson.badgerfish.data(ET.fromstring(json_data))  # Convert JSON to XML data

        # Convert XML data to an Element object
        #response_xml = ET.Element("response")
        #response_xml.extend(xml_data.values())

        # Convert Element object to a string
        #response = ET.tostring(response_xml, encoding="utf-8").decode("utf-8")

    return response


def parse_request_data(request_data=None, output_format="json"):
    try:
        # Try parsing as JSON
        json_data = json.loads(request_data)
        return "json", json_data
    except json.JSONDecodeError:
        # if accept header includes the string "xml" than don't cast the request_data to string
        if output_format == "xml":
            try:
                xml_data = ET.fromstring(request_data)
                return "xml", ET.tostring(xml_data, encoding='utf-8').decode('utf-8')
            except ET.ParseError as e:
                # TODO handle the exception
                print(e)
                return "text", request_data
        else:
            try:
                # Try parsing as XML
                xml_data = ET.fromstring(request_data)
                #return "xml", request_data
                return "xml", xmljson.badgerfish.data(xml_data)

            except ET.ParseError as e:
                print(e)
                # Treat as plain text
                return "text", request_data


def set_response_format(request):
    response_format = "xml" if re.search(r"application\/xml", request.headers["accept"]) else "json"
    return response_format
