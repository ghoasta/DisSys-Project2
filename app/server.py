import socket
import threading
from data_read import Data_read


class ClientThread(threading.Thread):

    def __init__(self, client_address, client_socket, identity):
        threading.Thread.__init__(self)
        self.c_socket = client_socket
        print("Connection no. " + str(identity))
        print("New connection added: ", client_address)

    def run(self):
        reply = ""
        print("Connection from : ", clientAddress)

        while True:
            data = self.c_socket.recv(2048)
            msg = data.decode()
            print("From client", msg)
            #exist = new_single.check_user_exist(msg)
            #print("Do the user exist >> ",exist)
            if (new_single.check_user_exist(msg)):
                msg = "User exist"
            else:
                msg = "User does not exist"
            self.c_socket.send(bytes(msg, 'UTF-8'))
        print("Client at ", clientAddress, " disconnected......")


LOCALHOST = "127.0.0.1"
PORT = 64001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server started")
print("Waiting for client request..")
new_single = Data_read()
#print(new_single.print_user("E001"))

counter = 0

while True:
    server.listen(1)
    my_socket, clientAddress = server.accept()
    counter = counter + 1
    new_thread = ClientThread(clientAddress, my_socket, counter)
    new_thread.start()
