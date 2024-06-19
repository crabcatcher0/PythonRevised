import socket

port = 3000
CHUNK = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#instead of explicitely binding the socket, we will let os do it
#os will bind this for us

host = '127.0.0.1'
while True:
    s.connect((host, port))
    message = input("Type Your Message: ")
    data = message.encode('ascii')
    s.send(data)
    #data recieved
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"Message: {text}")
