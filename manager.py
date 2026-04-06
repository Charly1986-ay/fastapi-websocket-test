from fastapi.websockets import WebSocket


class WebSocketManager:
    def __init__(self):
        self.connected_clients = []

    async def connect(self, websocket: WebSocket) -> None:
        client_ip = f'client {websocket.client.host}: {websocket.client.port}'

        # client has connected
        await websocket.accept()        
        print(f'client {websocket.client.host}: {websocket.client.port}')

        # add client to list of connected clients
        self.connected_clients.append(websocket)
        print(f'Connected clients: {self.connected_clients}')

        # send welcome message to the client
        message = {
            'client': client_ip,
            'message': f'Welcome {client_ip}'
        }
        await websocket.send_json(message)


    async def send_message(self, websocket: WebSocket, message: dict) -> None:
        message = {
            'client': f'{websocket.client.host}: {websocket.client.port}',
            'message': message,
        }

        await websocket.send_json(message)
    
    async def disconnecet(self, websocket: WebSocket) -> None:
        self.connected_clients.remove(websocket)

        print(f'client {websocket.client.host}: {websocket.client.port} disconnected')

        print(f'Connected clients: {self.connected_clients}')