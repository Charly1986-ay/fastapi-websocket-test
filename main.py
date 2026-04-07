from sys import exc_info
from unittest import async_case

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
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
    await manager.connect(websocket)

    while True:
        try:
            message = await websocket.receive_json()
            print(f'Received message: {message}')

            for client in manager.connected_clients:
                await manager.send_message(client, message)
        except WebSocketDisconnect:
            await manager.disconnecet(websocket=websocket)