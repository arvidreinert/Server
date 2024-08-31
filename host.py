#http127.0.0.1 port 9000
# echo-server.py
import pickle
import socket
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9000  # Port to listen on (non-privileged ports are > 1023)
players_connected = {}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
while True:
    data,addr = s.recvfrom(4096)
    if data == b"get_me_the_others_location":
        pass
        #pickle.dumps(players_connected)
        #s.sendto(players_connected, addr)

    elif b"adp(" in data:
        encoded_string = pickle.loads(data)
        encoded_list = list(encoded_string)
        print(encoded_list)
        encoded_string = ""
        for i in range(4,len(encoded_list)-1):
            encoded_string += str(encoded_list[i])
        print(encoded_string)
        players_connected[f"{addr}"] = encoded_string
        s.sendto(pickle.dumps(encoded_string),addr)
