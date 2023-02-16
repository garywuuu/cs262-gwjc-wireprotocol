import socket
import select
import sys

from _thread import *

# map usernames to IP info
clients = {}

#list of active users by username -> ie john, jerry, jack
active_users = []

# map username to list of undelivered messages
undelivered_messages = {}

# do everything by user info 
def threaded(user):
	msg = "What's your username?"
	user.send(msg.encode('UTF-8'))
	username = (user.recv(1024)).decode('UTF-8')

	# checks to make sure not taken etc
	dupe = False
	if  user in clients.values():
		msg = "User already exists, create new account."
		user.send(msg.encode('UTF-8'))
		dupe = True
	if username in clients.keys():
		clients[username] = user
		print(username + " added to server!")
		msg = "Welcome to Chat262, " + username +"!"
		user.send(msg.encode('UTF-8'))
		active_users.append(username)

	# new account
	elif dupe == False:
		clients[username] = user
		undelivered_messages[username] = []
		print(username + " added to server!")
		msg = "Welcome to Chat262, " + username +"!"
		user.send(msg.encode('UTF-8'))
		active_users.append(username)

	deliver_undelivered(username)
	while True:
		#each time a new thread is created, deliver the messages sent while user was offline

		try:
			data = (user.recv(1024)).decode('UTF-8')
			if not data:
				active_users.remove(username)
				user.close()
				print(username + " Disconnected")
			data_list = data.split('|')	
			task = data_list[0]
			
			check_operations(task, user, data_list, username)

		except:
			user.close()
			return False

def check_operations(task, user, data_list, username):
	# Feature 2: listing all accounts
	if task == "list":
		try:
			list_accounts(user)
			print("Listed users")
		except:
			print("Error in listing accounts")

	# Feature 3: sending a message
	elif task == "send":
		# quick check to see valid format
		if len(data_list) != 3:
			msg = "Invalid Command"
			user.send(msg.encode('UTF-8'))
			return False

		print("valid command")
		# user must specify who they want to send a message to
		receiver_username = data_list[1]
		message = ("From " + username + ": "+ data_list[2]).encode('UTF-8')
		if receiver_username in clients.keys():
			if receiver_username in active_users:
				sendmessage(message, receiver_username)
				print("sent message")
			else:
				undelivered_messages[receiver_username].append(message)
				print("message_queued")
				print(undelivered_messages[receiver_username])
				# message = "message queued"
				# user.send(message.encode('UTF-8'))
		else:
			print("recipient not a user")

	# Feature 4: removing user from network
	elif task == "remove":
		remove(username)

def deliver_undelivered(username):
	for msg in undelivered_messages[username]:
		clients[username].send(msg)
		undelivered_messages.pop(msg)


def sendmessage(message, receiver_username):
	try:
		clients[receiver_username].send(message)
	except:
		clients[receiver_username].close()


def list_accounts(recipient):
	users = "Users = "+''.join(str(n)+" | " for n in active_users)
	print(users)
	recipient.send(users.encode('UTF-8'))


def remove(username):
	if username in clients.keys():
		clients.pop(username)
		active_users.pop(username)
		clients[username].close()


def Main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


	# takes the first argument from command prompt as IP address
	IP = "127.0.0.1"
	port=5001
	# takes second argument from command prompt as port number

	server.bind((IP, port))

	server.listen(100)
	print("Listening on port " + str(port))
	print(IP) 
	
	while True:
 
		# establish connection with client
		user, addr = server.accept() 
		print (addr[0] + " connected")	
		print('Connected to :', addr[0], ':', addr[1])
		# Start a new thread and return its identifier
		start_new_thread(threaded, (user,))
		
	server.close()

if __name__=='__main__':
    Main()