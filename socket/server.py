import socket 
import threading

# in uppercase for CONSTANT values
HEADER = 64
PORT = 5050
# SERVER = '192.168......' #address of the server i.e. this computer address for now
SERVER = socket.gethostbyname(socket.gethostname()) #instead of hardcoding like above
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONN_MSG = "DISCONNECTED!!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn ,addr):
    print(f"[NEW CONNECTION] : {addr} connected ")

    connected = True
    while connected:
        # "blocking line" = waits/blocks until its requirement met
        msg_length = conn.recv(HEADER).decode(FORMAT) # "blocking" req being a message sent from client

        if msg_length:
            msg_length = int(msg_length)

            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONN_MSG:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("msg received ".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")

    while True:
        conn, addr = server.accept() # 'blocking; where requirement is waiting for a server to connect
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1 }")


print("[STARTING] server is starting....")
start()
