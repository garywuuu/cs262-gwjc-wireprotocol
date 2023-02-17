import socket

def Main():
	host = "127.0.0.1"

	# Define the port on which you want to connect
	port = 5001

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# connect to server on local computer
	server.connect((host,port))

	while True:
		# message sent to server
		# message received from server
		# ask the client whether he wants to continue
		ans = input('\nEnter your request:')
		if ans == 'Quit':
			ans2 = input('\nDo you want to exit?(y/n) :')
			if ans2 =='y':
				continue
			else:
				break
		server.send(ans.encode('ascii'))
		data = server.recv(1024)
		# print the received message
		# here it would be a reverse of sent message
		print('Received from the server :',str(data.decode('ascii')))
		continue

	server.close()

if __name__ == '__main__':
	Main()



# hostname=socket.gethostname()  
# IP=socket.gethostbyname(hostname) 

# def Main():
#     port = 4007
    
#     server = (("10.250.113.135", port))
    
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.bind(server)
    
#     message = input("-> ")
#     while message !='q':
#         s.sendto(message2.encode('utf-8'), server)

#         data, addr = s.recvfrom(1024)
#         data = data.decode('utf-8')
#         print("Received:" + data)
#         message = input("-> ")
#     s.close()

# if __name__=='__main__':
#     Main()
