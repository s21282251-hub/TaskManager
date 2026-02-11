from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import uvicorn, os, requests

load_dotenv()
APP_ID = os.getenv('APP_ID')
app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get('/')
async def temperature_graph(request: Request):
    data = {}
    try:
        params = {
            "key": APP_ID,
            "q": "auto:ip"
        }
        res = requests.get("http://api.weatherapi.com/v1/current.json", params=params)
        data = res.json()
        print(data)

    except Exception as e:
        print("Exception:", e)

    return templates.TemplateResponse("weather.html", {
        "request": request,
        "data": data
    })


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
