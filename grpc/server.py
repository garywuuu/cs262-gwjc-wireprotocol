from concurrent import futures

import grpc
import time
import logging

import chat_pb2 as chat
import chat_pb2_grpc as rpc

class ChatServer(rpc.ChatServerServicer):  # inheriting here from the protobuf rpc file which is generated

    def __init__(self):
        # List with all the chat history
        self.chats = [] # need to edit so you have multiple chat lists
        self.clients = {}

    # The stream which will be used to send new messages to clients
    def ChatStream(self, request_iterator, context):
        """
        This is a response-stream type call. This means the server can keep sending messages
        Every client opens this connection and waits for server to send new messages

        :param request_iterator:
        :param context:
        :return:
        """
        lastindex = 0
        # For every client a infinite loop starts (in gRPC's own managed thread)
        while True:
            # Check if there are any new messages
            while len(self.chats) > lastindex: 
                n = self.chats[lastindex] #make sure to pull from one specific list, not just global list
                lastindex += 1
                yield n # look at yield = return

    def SendMessage(self, request: chat.Message, context):
        """
        This method is called when a clients sends a Note to the server.

        :param request:
        :param context:
        :return:
        """
        print("[{}] {}".format(request.username, request.message))
        self.chats.append(request)
        return chat.Empty()  
    
    def Signup(self, request: chat.SignupRequest, context):
        n = chat.SignupReply()
        username = request.username
        if username in self.clients.keys():
            n.success = False
            n.error = "Username already exists."
            print("Signup from {} failed: User already exists.".format(username))
        else:
            n.success = True
            self.clients[username] = {"active": True, "queue": []}
            print("New user {} has arrived!".format(username))
        return n

    def Login(self, request: chat.LoginRequest, context):
        n = chat.LoginReply()
        username = request.username
        # check if user exists
        if username not in self.clients.keys():
            n.success = False
            n.error = "No existing user found."
            print("Nonexistent user login request from {}".format(username))
        else:    
            # check if duplicate active user
            if self.clients[username]["active"]:
                n.success = False
                n.error = "You are already logged in elsewhere."
                print("Duplicate user login request from {}.".format(username))
            else:
                n.success = True
                self.clients[username]["active"] = True
                # ADD FLUSHING QUEUED MESSAGES
        return n

    def Logout(self, request: chat.LogoutRequest, context):
        n = chat.LogoutReply()
        username = request.username
        if username not in self.clients.keys():
            n.success = False
            n.error = "No existing user found."
            print("Nonexistent user logout request from {}".format(username))
        else:
            self.clients[username]["active"] = False
            n.success = True
            print("{} left the chat.".format(username))
        return n

    def List(self, request: chat.ListRequest, context):
        n = chat.ListReply()
        for user in self.clients.keys():
            n.users.append(user)
        print("Accounts listed.")
        n.success = True
        return n

    # new functions for creating account, listing accounts, etc in addition to sendnote

if __name__ == '__main__':
    port = 11912 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # create a gRPC server
    rpc.add_ChatServerServicer_to_server(ChatServer(), server)  # register the server to gRPC
    print('Starting server. Listening...')
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    while True:
        time.sleep(64 * 64 * 100)
