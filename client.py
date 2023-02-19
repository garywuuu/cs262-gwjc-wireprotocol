import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('UTF-8')
            print(message)
        except:
            print('Error receiving message from server')
            client.close()
            break


def send():
    while True:
        ans = input('\n')
        client.send(ans.encode('UTF-8'))
        

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()