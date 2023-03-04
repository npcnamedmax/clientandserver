from socket import *


serverPort = #serverport

serverAddr = '' #serverip

proxyLisSock = socket(AF_INET, SOCK_STREAM)

proxyLisSock.bind(("", serverPort))

proxyLisSock.listen(1)


while True:

    print("Ready to serve...\n")

    proxyCliSock, cliAddr = proxyLisSock.accept()

    print("Received a connection from: ", cliAddr, "\n")

    message = proxyCliSock.recv(1024).decode()

    print("Message from client is: ", message, "\n")

    if message == "close":

        break

    filename = message.split()[1].split("/")[4]

    print("File name is: ", filename, "\n")

    fileExist = "false"  # intialise file at cache as false

    filetouse = "" + filename  # path to cache

    print("path is: ", filetouse, "\n")

    try:  # if file is available in cache

        with open(filetouse, "r", encoding="utf-8-sig") as f:

            outputdata = f.read()

        proxyCliSock.send(outputdata.encode())

        fileExist = "true"

        print("Read from cache\n")

    except IOError:

        if fileExist == "false":  # file x exist in cache

            proxySerSock = socket(AF_INET, SOCK_STREAM)

            try:

                proxySerSock.connect((serverAddr, serverPort))

                filepath = "" + filename #path to directory of file in server

                request = "GET " + filepath + " HTTP/1.1"

                proxySerSock.send(request.encode())

                datafromser = proxySerSock.recv(1024).decode()

                if datafromser[0] == "404":

                    outputdata = "404 file not found on server"

                    proxyCliSock.send(outputdata.encode())

                else:

                    proxyCliSock.send(
                        datafromser.encode()
                    )  # send from server to client

                    tmpFile = open(
                        filetouse, mode="w"
                    )  # cr8 & write to a file in cache

                    tmpFile.write(datafromser)

                    tmpFile.close()

            except:

                print("illegal request\n")

                outputdata = "illegal request\n"

                proxyCliSock.send(outputdata.encode())

        proxySerSock.close()

    proxyCliSock.close()


proxyLisSock.close()
