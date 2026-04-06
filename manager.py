from fastapi.websockets import WebSocket


class WebSocketManager:
    def __init__(self):
        self.connected_clients = []

    async def connect(self, websocket: WebSocket) -> None:
        print(f'client {websocket.client.host}: {websocket.client.port}')

        self.connected_clients.append(websocket)

        print(f'Connected clients: {self.connected_clients}')


    async def send_message(self, websocket: WebSocket, message: str):
        message = {
            'client': f'{websocket.client.host}: {websocket.client.port}',
            'message': message
        }

        await websocket.send_json(message=message)
    
    async def disconnecet(self, websocket: WebSocket):
        self.connected_clients.remove(websocket)

        print(f'client {websocket.client.host}: {websocket.client.port} disconnected')

        print(f'Connected clients: {self.connected_clients}')