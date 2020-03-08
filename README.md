# basicWebsocket-impl
Basic WebSocket implementation

## To run
(Written in Python 3.6.9)
Clone and run server

```
pip3 install flask_socketio
pip3 install flask_cors
pip3 install flask
python3 server.py
```
(Probably don't need all the items in requirements.txt but I forgot to create a new venv)

Open index.html

Press the button

## Whats going on here?
Server is written in python, client is written in Javascript. When you click the button it runs the method in client.js that connects to the backend and sends a message.

When there is a connection on backend, the server sends a message back.

When the front end recieves a message it prints it to the console.

This is a demostration of basic event handling with websockets.

cheers.