from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jah123'
socketio = SocketIO(app)

@app.route('/')
def index():
    """Por defecto va directamente a la carpeta templates a buscar el archivo html"""
    return render_template("index.html")

@socketio.on("message")
def handleMessage(msg):
    print("Message: " + msg)

if __name__ == '__main__':
    socketio.run(app)
