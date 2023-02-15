import socket
import select
import sys

from _thread import *

clients = {}
active_users = []

undelivered_messages = {}

# do everything by username and address
def threaded(user, addr):
	msg = "Hello there"
	user.send(msg.encode('ascii'))
	username = ""
	for k, v in clients.items():
		if user == v:
			active_users.append(k)
			username = k

	while True:
		data = user.recv(1024)
		data_str = data.decode('ascii')

		if not data:
			print("No message")
			break

		data_list = data_str.split('|')	

		task = data_list[0]
		
		if task == "1":
			# checks to make sure not taken etc
			username = data_list[1]
			print(username)
			dupe = False
			# for u, info in clients.items():
			# 	if user == info:
			# 		msg = "User already exists."
			# 		user.send(msg.encode('ascii'))
			# 		dupe = True
			if dupe == False:
				clients[username] = user
				print(username + " added to server!")
				msg = "Welcome to Chat262, " + username +"!"
				user.send(msg.encode('ascii'))
				active_users.append(username)

		elif task == "2":
			list_accounts(user)
			print("Listed users")

		elif task == "3":
			if len(data_list) != 3:
				msg = "Invalid Command"
				user.send(msg.encode('ascii'))
				return False
			print("valid command")
			receiver_username = data_list[1]
			message = "From " + username + ": "+ data_list[2] 
			message = message.encode('ascii')
			if receiver_username in clients.keys():
				if receiver_username in active_users:
					sendmessage(message, receiver_username)
					print("sent message")
				else:
				#add to queue of unread messages
					pass
			else:
				print("recipient not a user")

		elif task == "4":
			remove(username)

		else:
			msg = "Invalid Command"
			user.send(msg.encode('ascii'))

			

def sendmessage(message, receiver_username):
	try:
		clients[receiver_username].send(message)
	except:
		clients[receiver_username].close()


def list_accounts(recipient):
	users = "Users = "+''.join(str(n)+" | " for n in active_users)
	print(users)
	recipient.send(users.encode('ascii'))


def remove(username):
	if username in clients.keys():
		clients.pop(username)
		active_users.pop(username)


def Main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


	# takes the first argument from command prompt as IP address
	IP = "127.0.0.1"
	port=5000
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
		start_new_thread(threaded, (user, addr[0]))
		
	server.close()

if __name__=='__main__':
    Main()