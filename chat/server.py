import socket

CHUNK = 65535 #recieve at most these bytes of data at a time
port = 3000
#create a socket object
#syntax socket.socket(family, type)
#AF_NET family of ipv4 ip address
#type SOCK_DGRAM udp, SOCK_STREAM: tcp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#some ip address that the server will listen 

hostname = '127.0.0.1' #ip of local machine
s.bind((hostname, port)) #bind the socket with this host machine and on port 3000

print(f"Server is live on {s.getsockname()}")

# run this server till i stop manually.

while True:
    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii') #data by default travels in byte
    print(f"{clientAdd} says: {message}")
    message_send = input("Reply: ")
    data = message_send.encode('ascii')
    # send data to the ip add that sent me the data
    s.sendto(data, clientAdd)