
import threading
from tkinter import *
from tkinter import simpledialog

import grpc

import ex_chat_pb2 as chat
import ex_chat_pb2_grpc as rpc

address = 'localhost'
port = 11912



class Client:

    def __init__(self, u: str):
        # create a gRPC channel + stub
        self.username = u
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.conn = rpc.ChatServerStub(channel)
        # create new listening thread for when new message streams come in
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    def __listen_for_messages(self):
        """
        This method will be ran in a separate thread as the main/ui thread, because the for-in call is blocking
        when waiting for new messages
        """
        for note in self.conn.ChatStream(chat.Empty()):  # this line will wait for new messages from the server!
            # print("R[{}] {}".format(note.name, note.message))  # debugging statement
            pass

    def send_message(self, message):
        """
        This method is called when user enters something into the textbox
        """
        if message != '':
            n = chat.Note()  # create protobug message (called Note)
            n.name = self.username  # set the username
            n.message = message  # set the actual message of the note
            print("S[{}] {}".format(n.name, n.message))  # debugging statement
            self.conn.SendNote(n)  # send the Note to the server

if __name__ == '__main__':
    username = None
    while username is None:
        # retrieve a username so we can distinguish all the different clients
        username = input("Enter username:")
    c = Client(username)
    print("Send a message!")
    while True:
        message = input('\n')
        c.send_message(message)
    # input, send_message 
