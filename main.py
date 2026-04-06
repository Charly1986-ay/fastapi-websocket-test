from unittest import async_case

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from manager import WebSocketManager

templates = Jinja2Templates(
    directory='templates/'
)

app = FastAPI()
# Montar la carpeta "static" en la ruta "/static"
app.mount(
    "/static", 
    StaticFiles(directory="static"), name="static"
)

manager = WebSocketManager()

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {}
    )

@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket=websocket)

    while True:
        message = await websocket.receive_json()

        await manager.send_message(websocket=websocket, message=message)