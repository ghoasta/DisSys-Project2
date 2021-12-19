import json
import os
import sys
import pika

def callback(ch, method, properties, body):
    f = open("audit_log.txt", 'a+')
    queue = json.loads(body)
    audit_string = "||Timestamp: " + queue[1] + "||IP Address & Port: " + str(queue[0]) + "||Empno: " \
                  + queue[2] + "||Commands: " + queue[3] + "-" + queue[4] + "||"
    f.write(audit_string + "\n")
    f.close()
    print(audit_string)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='audit-rabbit')

    channel.basic_consume(queue='audit-rabbit',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)