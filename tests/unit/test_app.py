import pytest
from flask import Flask
from flask_sock import Sock



        

def test_websocket(client):
    client.get('/ws')
    assert client.is_upgraded()
    client.send_message('Hello')
    assert client.get_received() == 'Hello'