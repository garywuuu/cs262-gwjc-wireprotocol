
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

    def thread(self):
        if self.username is not None:
            # create new listening thread for when new message streams come in
            threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    def __listen_for_messages(self):
        """
        This method will be ran in a separate thread as the main/ui thread, because the for-in call is blocking
        when waiting for new messages
        """
        if self.username is not None:
            n = chat.ConnectRequest()
            n.recipient = self.username
            for connectReply in self.conn.ChatStream(n):  # this line will wait for new messages from the server!
                if connectReply.active:
                    print("R[{}] {}".format(connectReply.sender, connectReply.message)) 
                else: # need to return to terminate thread
                    return

    def send_message(self, message, recipient):
        """
        This method is called when user enters something into the textbox
        """
        if recipient != '' and message != '':
            n = chat.MessageRequest()  # create protobug message (called Note)
            n.sender = self.username  # set the username
            n.recipient = recipient 
            n.message = message
            print("S[{} -> {}] {}".format(n.sender, n.recipient, n.message)) 
            reply = self.conn.SendMessage(n)  # send to the server
            if reply.success:
                pass
            else:
                print("{}".format(reply.error))
        else:
            print("Please enter a recipient and a message.")

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
            self.username = None
            print("Logout successful!")

    def list(self, query):
        n = chat.ListRequest()
        n.query = query
        reply = self.conn.List(n)
        if reply.success:
            for user in reply.users:
                print(user)
        else:
            print("{}".format(reply.error))

    def delete(self):
        n = chat.DeleteRequest()
        n.username = self.username
        self.logout()
        reply = self.conn.Delete(n)
        if reply.success:
            print("Account deleted.")
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
            c.thread()
            print("Commands: \send to send a message, \logout to log out, \list to list accounts, \delete to delete your account.")
            while c.username is not None:
                request = input('')
                if request == "\logout":
                    c.logout()
                elif request == "\list":
                    # include wildcard ***
                    query = input("Query: ")
                    c.list(query)
                elif request == "\send":
                    recipient = input("Recipient: ")
                    message = input("Message: ")
                    c.send_message(message, recipient)
                elif request == "\delete":
                    confirm = input("Are you sure you want to delete your account? [y]: ")
                    if confirm == "y":
                        c.delete()
                    else:
                        print("Account deletion cancelled.")
                else:
                    print("Please enter a valid command.")
    except KeyboardInterrupt:
        if c.username is not None:
            c.logout()
