from socket import *

import sys


serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = #insert port

serverSocket.bind(("", serverPort))

serverSocket.listen(1)

while True:

    print("Ready to serve..")

    connectionSocket, addr = serverSocket.accept()

    print(
        "connectionSocket name: ",
        connectionSocket.getsockname(),
        "\n",
        "serverSocket name: ",
        serverSocket.getsockname(),
        "\n",
    )

    print("address of client: ", addr, "\n")

    try:

        message = connectionSocket.recv(1024).decode()

        filename = message.split()[1]

        with open(filename, "r", encoding="utf-8-sig") as f:

            string = f.read()

        outputdata = "HTTP/1.1 200 ok\r\n Host: servername\r\n\r\n" + string

        connectionSocket.send(outputdata.encode())  

        connectionSocket.send("\r\n".encode())

        print("Successfully sent\n")

        connectionSocket.close()

    except IOError:

        connectionSocket.send("404 Not Found".encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

        serverSocket.close()

        sys.exit()

    serverSocket.close()

    sys.exit()


