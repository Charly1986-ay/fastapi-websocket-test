const ws = new WebSocket("ws://localhost:8000/ws");
const form = document.querySelector('form');
const messagesDiv = document.getElementById('messages');
const clientIdSpan = document.getElementById('client-id');

// Create a unique identifier for each client
const makeid = (length) => {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;

    while (counter < length) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
        counter += 1;
    }

    return result;
};

const clientIdentifier = makeid(6);
clientIdSpan.innerText = clientIdentifier;

ws.onopen = () => {
    // Client is connected
    console.log('Connected to WebSocket Server');
    ws.send(JSON.stringify({
        content: `${clientIdentifier} joined`,
        client: clientIdentifier,
        timestamp: new Date().getTime()
    }));
};

ws.onmessage = (event) => {
    // Receiving a message
    const data = JSON.parse(event.data);
    const newMessage = document.createElement('p');
    newMessage.innerText = `${data.client} says ${data.message}`;
    messagesDiv.appendChild(newMessage);

    const hr = document.createElement('hr');
    messagesDiv.appendChild(hr);
};

ws.onerror = (error) => {
    console.error('WebSocket Error:', error);
};

ws.onclose = () => {
    console.log('WebSocket connection closed');
};

form.addEventListener('submit', async (event) => {
    // Submitting event
    event.preventDefault();

    const formData = new FormData(form);
    const message = formData.get('message');

    ws.send(JSON.stringify({
        content: message,
        client: clientIdentifier,
        timestamp: new Date().getTime()
    }));

    form.reset();
});