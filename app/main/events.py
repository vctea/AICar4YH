from flask_socketio import emit
from ..import socketio

name_space = '/ws'

@socketio.on('connect', namespace=name_space)
def connect():
    print('client connected.')

@socketio.on('disconnect', namespace=name_space)
def disconnect():
    print('client disconnected.')

@socketio.on('myEvent', namespace=name_space)
def myEvent(data):
    print('myEvent!!!')
    print(data)

@socketio.on('forward', namespace=name_space)
def forward(data):
    print('forward')
    print(data)

@socketio.on('retreat', namespace=name_space)
def retreat(data):
    print('retreat')
    print(data)

@socketio.on('left', namespace=name_space)
def left(data):
    print('left')
    print(data)

@socketio.on('right', namespace=name_space)
def left(data):
    print('right')
    print(data)

@socketio.on('stop', namespace=name_space)
def left(data):
    print('stop')
    print(data)