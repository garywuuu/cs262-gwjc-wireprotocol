'Chat Room Connection - Client-To-Client'
import threading
import socket
host = '127.0.0.1'

port = 59001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = {}
active_users = []
undelivered_messages = {}



def handle_client(user):
	username = ""
	for k, v in clients.items():
		if user == v:
			if k in active_users:
					pass
			else:
				active_users.append(k)
				username = k
	while True:
		try:
			data = (user.recv(1024)).decode('UTF-8')
			data_list = data.split('|')	
			task = data_list[0]
			check_operations(task, user, data_list)
		
		except:
			active_users.pop(username)
			del clients[username]
			user.close()
			print("User disconnected")

		
def check_operations(task, user, data_list):
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

def receive():
	while True:
		print('Server is running and listening ...')
		client, address = server.accept()
		print(f'connection is established with {str(address)}')
		client.send('you are now connected!'.encode('utf-8'))
		thread = threading.Thread(target=handle_client, args=(client,))
		thread.start()
if __name__ == "__main__":
    receive()