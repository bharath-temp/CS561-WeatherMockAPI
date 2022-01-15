import requests
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
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=corvallis&appid=a99f1dbe7d7e7d5b6ce85970a31da042')
    return r.json()

def server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port="80")