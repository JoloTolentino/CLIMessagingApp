from flask import Flask
from flask_sock import Sock
from utils import *


app = Flask(__name__)
sock = Sock(app)

connected_users = set()


@sock.route("/connect")
def handle_message(ws):
    connected_users.add(ws)
    ws.send("Welcome to CLI Messaging")
    ws.send("enter a username")
    user_name = None
    while True:
        user_name = ws.receive()
        if user_name:
            break
    enter_chat(ws, user_name)


def enter_chat(ws, user_name):
    CRUD = {
        'get': {
            'news':utils.get_news,
            'nba': utils.get_nba,
        },
        'post': {
            'news':utils.post_news,
        },
        'update': {
            'news': utils.update_news,
            'nba' : utils.update_nba,
        }
    }
    while True:
        text = ws.receive()
        if text == "dc":
            connected_users.remove(ws)
            ws.send("{} logging out".format(user_name))
            break

        #depends on the context

        for user in connected_users:
            if text and text[0] == '/':
                command = text[1:]
                crud,data = command.split('-')
                response =CRUD[crud][data]()
                user.send("{}".format(response))    
            user.send("{} : {}".format(user_name, text))


