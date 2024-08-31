# echo-client.py
import pickle
import socket
my_pos = (0, 10, 40)
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #b befor ""
    l = pickle.dumps(list)
    s.sendall(l)
    data = s.recv(1024)

print(pickle.loads(data))