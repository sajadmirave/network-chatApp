import socket
from colorma import Fore
# create connection

# to connection we need ip, port
# Af_INEt (ip v4)
ipv4 = socket.AF_INET
port = socket.SOCK_STREAM  # tcp


server = socket.socket(ipv4, port)


address = "192.168.1.104"
# new connection
server.bind(tuple((address, 4445)))


# listen the port
maxConnection = 1
server.listen(maxConnection)


# send message
print("Server Is Running On Port 4445 ...")


# dont close connection
client, clientAdress = server.accept()

print(f"{clientAdress} is connected")

# send data to client
while True:
    client.send("Hello Client :D".encode())
    # get data
    size = 1204
    message = client.recv(size).decode()
    print("Client:", message)

    # send data
    serverMessage = input("Enter Your Message: ")
    client.send(serverMessage.encode())

    if serverMessage == "close":
        # close connection
        server.close()
