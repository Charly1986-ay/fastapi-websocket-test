from fastapi import FastAPI, APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates/')

app = FastAPI()
router = APIRouter()

# Montar la carpeta "static" en la ruta "/static"
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def form(request: Request):
    return templates.TemplateResponse(
        request,
        "ws/chat.html",
        {"request": request}
    )

@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            print('Conectando...')
            # recibe el servidor un mensaje del usuario
            data = await websocket.receive_text()
            # le devuelve una respuesta
            await websocket.send_text(f'Message text was: {data}')

    except WebSocketDisconnect:
        print('El cliente cerró la conexión')

    except Exception as e:
        print(f'Error inesperado: {e}')

    finally:
        #--- Logica Final ---
        print('limpieza finalizada')