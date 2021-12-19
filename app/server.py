import json
import os
import socket
from dataread import DataRead
import pika
from datetime import datetime

# receiving message from client
import threading


def to_audit_queue(message):
    # Send message to RabbitMQ and the close connection.
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        channel = connection.channel()
        channel.queue_declare(queue="audit-rabbit") #logging
        channel.basic_publish(exchange="", routing_key="audit-rabbit", body=json.dumps(message))
        connection.close()
    except pika.exceptions.AMQPConnectionError:
        print("Could not post to RabbitMQ")


def newClient(con):
    now = datetime.now()
    print("Connection from : ", adr)
    while True:
        empno = con.recv(4096)
        print("Employee id1 : " + empno.decode())
        exist = new_single.check_user_exist(empno.decode())
        if exist:
            con.send("VALID".encode())
            command1 = con.recv(4096)
            command1 = command1.decode()
            if command1 == 'S':
                con.send('S'.encode())
                command2 = con.recv(4096)
                command2 = command2.decode()
                if command2 == 'C':
                    print("From: ",adr," Commands: ",command1,"->",command2)
                    name = new_single.get_name(empno.decode())
                    current_salary = new_single.get_current_salary(empno.decode())
                    mes = "Employee: " + name + "\nCurrent basic salary: " + str(current_salary)
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    message = [adr, dt_string, empno.decode(), command1, command2]
                    to_audit_queue(message)
                    con.send(mes.encode())

                elif command2 == 'T':
                    print("From: ", adr, " Commands: ", command1, "->", command2)
                    command3 = con.recv(4096)
                    command3 = command3.decode()
                    basic, overtime = new_single.get_salary_year(empno.decode(), command3)
                    mes = "Employee: " + new_single.get_name(
                        empno.decode()) + "\nTotal Salary for year: " + command3 + ": " \
                         "Basic pay: " + str(basic) + "; Overtime: " + str(overtime)
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    message = [adr, dt_string, empno.decode(), command1, command2]
                    to_audit_queue(message)
                    con.send(mes.encode())

            if command1 == 'L':
                con.send('L'.encode())
                command4 = con.recv(4096)
                command4 = command4.decode()
                if command4 == 'C':
                    print("From: ", adr, " Commands: ", command1, "->", command4)
                    current_leave = new_single.get_current_leave(empno.decode())
                    print(current_leave)
                    mes = "Employee: " + new_single.get_name(
                        empno.decode()) + "\nCurrent annual leave entitlement: " + str(current_leave)
                    print(mes)
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    message = [adr, dt_string, empno.decode(), command1, command4]
                    to_audit_queue(message)
                    con.send(mes.encode())
                elif command4 == 'Y':
                    print("From: ", adr, " Commands: ", command1, "->", command4)
                    command5 = con.recv(4096)
                    command5 = command5.decode()
                    leave = new_single.get_year_annual(empno.decode(), command5)
                    print("LEAVE By year:", command5, " >> ", leave)
                    mes = "Employee: " + new_single.get_name(
                        empno.decode()) + "\nLeave taken in " + command5 + ": " + str(leave)
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    message = [adr, dt_string, empno.decode(), command1, command4]
                    to_audit_queue(message)
                    con.send(mes.encode())
        else:
            con.send("INVALID".encode())

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server started")
print("Waiting for client request..")
serv.bind(('127.0.0.1', 9856))
serv.listen(5)
new_single = DataRead()

counter = 0
while True:
    conn, adr = serv.accept()
    counter = counter + 1
    t1 = threading.Thread(target=newClient, args=(conn,))
    t1.start()
