
import threading
from tkinter import *
from tkinter import simpledialog

import grpc

import chat_pb2 as chat
import chat_pb2_grpc as rpc

address = 'localhost'
port = 11912



class Client:

    def __init__(self):
        # create a gRPC channel + stub
        self.username = None
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
            n = chat.Message()  # create protobug message (called Note)
            n.username = self.username  # set the username
            n.message = message  # set the actual message of the note
            print("S[{}] {}".format(n.username, n.message))  # debugging statement
            self.conn.SendMessage(n)  # send the Note to the server

    def signup(self, username):
        if username != '':
            n = chat.SignupRequest() 
            n.username = username
            reply = self.conn.Signup(n)
            if reply.success:
                self.username = n.username
                print("Signup successful!")
            else:
                print("{}".format(reply.error))

    def login(self, username):
        if username != '':
            n = chat.LoginRequest() 
            n.username = username
            reply = self.conn.Login(n)
            if reply.success:
                self.username = n.username
                print("Login successful!")
            else:
                print("{}".format(reply.error))

    def logout(self):
        n = chat.LogoutRequest()
        n.username = self.username
        reply = self.conn.Logout(n)
        if reply.success:
            c.username = None
            print("Logout successful!")

    def list(self):
        # include wildcard later ***
        n = chat.ListRequest()
        reply = self.conn.List(n)
        if reply.success:
            for user in reply.users:
                print(user)
        else:
            print("{}".format(reply.error))

if __name__ == '__main__':
    c = Client()
    try:        
        while c.username is None:
            req = input("Enter 1|{Username} to sign up or 2|{Username} to log in: ")
            if req[0:2] == "1|":
                c.signup(req[2:])
            elif req[0:2] == "2|":
                c.login(req[2:])
            else:
                print("Invalid input.")
            print("Send a message! Or, \logout to log out, \list to list accounts.")
            while c.username is not None:
                request = input('')
                if request == "\logout":
                    c.logout()
                elif request == "\list":
                    # include wildcard ***
                    c.list()
                else:
                    c.send_message(request)
    except KeyboardInterrupt:
        if c.username is not None:
            # logout user
            c.logout()
