import socket
from _thread import *
import sys

SERVER = "192.168.1.5"
PORT = 5555
# SERVER = "192.168.1.68"
# SERVER = socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connections.., Server Started!!")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected!!")
                break
            else:
                print("Reviced :", reply)
                print("Sending :", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
