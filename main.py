from unittest import async_case

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import websocket

templates = Jinja2Templates(
    directory='templates/'
)

app = FastAPI()
# Montar la carpeta "static" en la ruta "/static"
app.mount(
    "/static", 
    StaticFiles(directory="static"), name="static"
)

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {}
    )

@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    pass