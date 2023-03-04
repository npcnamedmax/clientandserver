# Use method: ./client.py (FILEPATH)


from socket import *


import sys


serverIP = "" #serverip


serverPort = #serverport

clientSocket = socket(AF_INET, SOCK_STREAM)


clientSocket.connect((serverIP, serverPort))


n = len(sys.argv)


if n != 2:

    s = input("Filepath: ")

    print("\n")

    filepath = s


else:

    filepath = sys.argv[1]


request = "GET " + filepath + " HTTP/1.1\r\nHost: " + serverIP + "\r\n\r\n"

clientSocket.send(request.encode())


message = clientSocket.recv(1024).decode()


print("Message from server: \n", message, "\n")


clientSocket.close()


sys.exit()
