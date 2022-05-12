from distutils.log import debug
from webapp import create_app
from webapp import socketio



app = create_app()

if __name__ == "__main__":
    socketio.run(app,host="172.20.10.3", port = 8001, debug = True)