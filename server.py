from socket import *

# Create a TCP/IP socket
def createServer():
    serversock = socket(AF_INET, SOCK_STREAM)
    # Bind the socket to the port
    try:
        serversock.bind(('', 4004))
        serversock.listen(5)
        while(1):
            (clientsock, address) = serversock.accept()

            rd = clientsock.recv(5000).decode()
            pieces = rd.split('\n')
            if (len(pieces) > 0):
                print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><head><title>My Simple Server</title></head>"
            data += "<body><p>Hello Dr460n4ir3!</p></body></html>\r\n\r\n"
            clientsock.sendall(data.encode())
            clientsock.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down server...\n")
    except Exception as e:
        print("Error: \n" + str(e))

    serversock.close()

print('Access http://localhost:4004/ in your browser')
createServer()
