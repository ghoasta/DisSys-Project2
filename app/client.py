import socket

# using socket to connect with server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# using the local server and the port 9856 on which the
# server will connect.
print("HR System 1.0")
client.connect(('127.0.0.1', 9857))
while True:

    empno = str(input("Enter Employee ID : "))
    empno = empno.strip().upper()
    client.send(empno.encode())
    status = client.recv(4096)
    #print("Status : " + status.decode())

    if status.decode() == "VALID":
        command1 = str(input("Salary (S) or Annual Leave (L) Query? >> "))
        command1 = command1.strip().upper()
        client.send(command1.encode())
        #print("Command1 == ",command1)

        comm1_reply = client.recv(4096)
        comm1_reply = comm1_reply.decode()
        print(comm1_reply)
        if comm1_reply == 'S':
            command2 = str(input("Current salary (C) or total salary (T) for year? "))
            command2 = command2.strip().upper()
            client.send(command2.encode())
            print("Command2 == ", command2)

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

        if comm1_reply == 'L':
            command4 = str(input("Current Entitlement (C) or Leave taken for year (Y)? "))
            command4 = command4.strip().upper()
            print("Command4 == ", command4)
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
        print("Sorry... I don’t recognise that employee id")
