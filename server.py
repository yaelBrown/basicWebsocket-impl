from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'wow-super-secret'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/test')
def index():
    return "The server is working"


# This is the socket method that sends the message back
@socketio.on('message')
def message(data):
  print(f"{data}")
  send(data)

# This is a example of a custom event sent to one client
@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

# This is a example of a custom event that is broadcast to multiple clients
@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

# These are example of the connect and disconnect events
@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    print("Running server")
    socketio.run(app, host="0.0.0.0")