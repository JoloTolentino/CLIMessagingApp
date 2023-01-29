from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)



connected_users = set()
@sock.route('/connect') 
def handle_message(ws):
    connected_users.add(ws)
    while True:
        text = ws.receive()
        if text == 'dc':
            connected_users.remove(ws)
            ws.send("disconnecting")
            break
        for user in connected_users:
            user.send(text)





# if __name__ == '__main__':
#     sock.run(app, host='0.0.0.0', port=8000)
