import socket
import select
import sys

from _thread import *

clients = {}
active_users = []

undelivered_messages = {}

# do everything by user info and username
def threaded(user):
	while True:
		username = ""
		for k, v in clients.items():
			if user == v:
				username = k
				if k in active_users:
					pass
				else:
					active_users.append(k)
		try:
			data = (user.recv(1024)).decode('UTF-8')
			data_list = data.split('|')	
			task = data_list[0]
			
			check_operations(task, user, data_list, username)

		except socket.error as e:
			active_users.pop(username)
			user.close()
			print(e)

def check_operations(task, user, data_list, username):
	if task == "1":
		# checks to make sure not taken etc
		username = data_list[1]
		print(username)
		dupe = False
		if username in clients.keys() or user in clients.values():
			msg = "User already exists, create new account."
			user.send(msg.encode('UTF-8'))
			dupe = True
		if dupe == False:
			clients[username] = user
			undelivered_messages[username] = []
			print(username + " added to server!")
			msg = "Welcome to Chat262, " + username +"!"
			user.send(msg.encode('UTF-8'))
			active_users.append(username)

	elif task == "2":
		list_accounts(user)
		print("Listed users")

	elif task == "3":
		if len(data_list) != 3:
			msg = "Invalid Command"
			user.send(msg.encode('UTF-8'))
			return False
		print("valid command")
		receiver_username = data_list[1]
		message = "From " + username + ": "+ data_list[2] 
		message = message.encode('UTF-8')
		if receiver_username in clients.keys():
			if receiver_username in active_users:
				sendmessage(message, receiver_username)
				print("sent message")
			else:
				undelivered_messages[username].append(message)
		else:
			print("recipient not a user")

	elif task == "4":
		remove(username)

def deliver_undelivered(user):
	username = ""
	for k, v in clients.items():
		if user == v:
			username = k
	for msg in undelivered_messages[username]:
		sendmessage(msg, username)


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