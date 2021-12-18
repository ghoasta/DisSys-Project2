import os
import socket
from dataread import DataRead

# receiving message from client
import threading

def newClient(con):
    print("Connection from : ", adr)
    while True:
        empno = con.recv(4096)
        print("Employee id1 : " + empno.decode())
        exist = new_single.check_user_exist(empno.decode())
        print(exist)
        if exist:
            con.send("VALID".encode())
            command1 = con.recv(4096)
            command1 = command1.decode()
            print("Command1 : " + command1)

            if command1 == 'S':
                con.send('S'.encode())
                command2 = con.recv(4096)
                command2 = command2.decode()
                print("Command2 : " + command2)
                if command2 == 'C':
                    name = new_single.get_name(empno.decode())
                    print("NAME >> ", name)
                    current_salary = new_single.get_current_salary(empno.decode())
                    print("CURRENT SALARY >> ", current_salary)
                    mes = "Employee: "+name+ "\nCurrent basic salary: "+str(current_salary)
                    print(mes)
                    con.send(mes.encode())
                elif command2 == 'T':
                    #con.send('T'.encode())
                    #print("years")
                    command3 = con.recv(4096)
                    command3 = command3.decode()
                    #print(command3)
                    basic, overtime = new_single.get_salary_year(empno.decode(),command3)
                    #print(basic, overtime)
                    mes = "Employee: "+new_single.get_name(empno.decode())+ "\nTotal Salary for year: "+command3+": " \
                         "Basic pay: "+str(basic)+"; Overtime: "+str(overtime)
                    #print(mes)
                    con.send(mes.encode())


            if command1 == 'L':
                con.send('L'.encode())
                command4 = con.recv(4096)
                command4 = command4.decode()
                print("Command4 >> ",command4)
                if command4 == 'C':
                    current_leave = new_single.get_current_leave(empno.decode())
                    print(current_leave)
                    mes = "Employee: "+new_single.get_name(empno.decode())+"\nCurrent annual leave entitlement: "+str(current_leave)
                    print(mes)
                    con.send(mes.encode())
                elif command4 == 'Y':
                    print("YEAR")
                    command5 = con.recv(4096)
                    command5 = command5.decode()
                    leave = new_single.get_year_annual(empno.decode(),command5)
                    print("LEAVE By year:",command5," >> ",leave)
                    mes = "Employee: "+new_single.get_name(empno.decode())+"\nLeave taken in "+command5+": "+str(leave)
                    con.send(mes.encode())



        else:
            con.send("INVALID".encode())




serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server started")
print("Waiting for client request..")
# binding port with ip and socket
serv.bind(('127.0.0.1', 9857))
serv.listen(5)
new_single = DataRead()

counter = 0
while 1:
    #print("Waiting for client")
    # waiting for client request
    conn, adr = serv.accept()
    ounter = counter + 1
    t1 = threading.Thread(target=newClient, args=(conn,))
    t1.start()

