import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        ans = input('\n')
        client.send(ans.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()