import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("HR System 1.0")
client.connect(('127.0.0.1', 9856))
while True:
    print("if you want to exit type X")
    empno = str(input("Enter Employee ID : "))
    empno = empno.strip().upper()
    client.send(empno.encode())
    status = client.recv(4096)

    if empno == 'X':
        sys.exit()

    if status.decode() == "VALID":
        command1 = str(input("Salary (S) or Annual Leave (L) Query? >> "))
        command1 = command1.strip().upper()
        client.send(command1.encode())
        comm1_reply = client.recv(4096)
        comm1_reply = comm1_reply.decode()
        if comm1_reply == 'S':
            command2 = str(input("Current salary (C) or total salary (T) for year? "))
            command2 = command2.strip().upper()
            client.send(command2.encode())
            if command2 == 'C':
                result = client.recv(4096)
                result = result.decode()
                print(result)
            elif command2 == 'T':
                command3 = input("What year? ")
                client.send(command3.encode())
                result = client.recv(4096)
                result = result.decode()
                print(result)
            else:
                print("Invalid command")

        elif comm1_reply == 'L':
            command4 = str(input("Current Entitlement (C) or Leave taken for year (Y)? "))
            command4 = command4.strip().upper()
            client.send(command4.encode())
            if command4 == 'C':
                result = client.recv(4096)
                result = result.decode()
                print(result)
            elif command4 == 'Y':
                command5 = input("What year? ")
                client.send(command5.encode())
                result = client.recv(4096)
                result = result.decode()
                print(result)
            else:
                print("Invalid command")
        else:
            print("Invalid command")

    else:
        print("Sorry... I don’t recognise that employee id")
