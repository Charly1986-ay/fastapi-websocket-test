const ws = new WebSocket("ws://localhost:8000/ws");

ws.onopen = () => {
    console.log('Connected to websocket Server');
}

ws.onmessage = (event) => {
    const message = JSON.parse(event.data);
    console.log(message);
    //console.log(`Received message: ${message}`);
}

ws.onerror = (error) => {
    console.error('Websocket Error:', error);
}

ws.onclose = () => {
    console.log('Websocket connection closed');
}

const form = document.querySelector('form');
//console.log(form);
form.addEventListener('submit', (event) => {
    const formData = new FormData(form);

    const message = formData.get('message');

    ws.send(JSON.stringify({type: 'text', content: message}));

    event.preventDefault();
});