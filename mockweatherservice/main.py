import requests
import os
import json

import boto3

from datetime import datetime
from typing import Optional
from fastapi import FastAPI


weather_api_key = 'a99f1dbe7d7e7d5b6ce85970a31da042'

app = FastAPI()

@app.get("/")
def read_root():
    return {"boo": "Worl243465"}


@app.get("/data/2.5/weather")
def read_item():
    #return {"item_id": item_id, "q": q}
    session = boto3.Session(
        aws_access_key_id=os.environ['MY_AWS_ACCESS_ID'],
        aws_secret_access_key=os.environ['MY_AWS_SECRET_KEY']
    )
    s3 = session.resource('s3')
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=corvallis&appid=a99f1dbe7d7e7d5b6ce85970a31da042')
    now = datetime.now()
    #date_time = now.strftime("%m-%d-%Y_%H:%M:%S")

    object = s3.Object('weatherapi-cs561-bharath', f"weather.json")
    result = object.put(Body=(bytes(json.dumps(r.json()).encode('UTF-8'))))

    res = result.get('ResponseMetadata')

    if res.get('HTTPStatusCode') == 200:
        print('File Uploaded Successfully')
    else:
        print('File Not Uploaded')

    return r.json()

def server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port="80")