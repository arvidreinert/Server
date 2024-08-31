#http127.0.0.1 port 9000
# echo-server.py
import pickle
import socket
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9000  # Port to listen on (non-privileged ports are > 1023)
players_connected = {}
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
      conn, addr = s.accept()
      #with conn
      print(f"Connected by {conn}, adress:{addr}")
      #Connected by (('127.0.0.1', 56514), <socket.socket fd=1000, family=2, type=1, proto=0, laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 56514)>)
      players_connected[f"{addr}"] = (0,0,0)
      print(len(players_connected))
      if len(players_connected) >= 2:
        break
    while True:
        data,addr = conn.recvfrom(1024)
        print(addr)
        if data == b"get_me_the_others_location":
            conn.sendto(pickle.dumps(players_connected), str(addr))