import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONN_MSG = "DISCONNECTED!!"
SERVER = "192.168.18.137"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))
send("yolo!!")
input()
send("yolo hola!!")
input()
send("yolo moshimosh!!")
input()
send("yolo pasaa!!")

send(DISCONN_MSG)
