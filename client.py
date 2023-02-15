# connect to server

import socket

# create connection

# to connection we need ip, port
# Af_INEt (ip v4)
ipv4 = socket.AF_INET
port = socket.SOCK_STREAM  # tcp


server = socket.socket(ipv4, port)

# output something when server will find :/

print("Find Server...")

address = "192.168.1.104"
# new connection
server.connect(tuple((address, 4445)))


# send message
print("Connected...")

# get data
size = 1204
# the data get from server is byte and here we are decode the data to show data

while True:
    message = server.recv(size).decode()
    print("Server:",message)

    # send daata
    clienctMessage = input("Enter Your Message: ")

    # encode for sending data(because the data is byte)
    server.send(clienctMessage.encode())

server.close()
