import socket

SERVER = "127.0.0.1"
PORT = 64001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client", 'UTF-8'))
print("HR System 1.0")

while True:
    in_data = client.recv(1024)
    print(in_data.decode())
    empno = input("What is employee ID? >> ")
    empno = empno.upper()
    #out_data = input()
    client.sendall(bytes(empno, 'UTF-8'))
    if empno == 'BYE':
        break

client.close()
