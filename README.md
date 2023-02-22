# CS262 Design Project 1

## Wire protocol Usage and setup: 

Clone the repository on each local computer that will be using the network (all clients and the server). 
Install requirements with ``pip install -r requirements.txt``

### For Server:
Run ``python3 server.py`` in base directory. This will allow the server to start listening to new clients that join and their commands. As clients join and make requests, important updates will be printed to the server command line. 

### For Clients:
 Run ``python3 client.py`` in base directory. 

### Instruction Flow and Command Structure:
Upon signup, you will be asked to enter your username. If you have an existing account, you will be logged into that account assuming no one else is logged into that account, otherwise a new account will be created with your associated IP. 

### Command Documentation:
#### Listing Accounts: 
To list accounts, you may either use the built-in list|all and list|active commands that list either all users in the network or just active users, or any character/set of characters ie. list|g. 
<br/><br/>

#### Sending Messages:
To send a message, you must use the following structure: list|recipient_username|message. If your command has a valid recipient username, then one of two events will occur. 

    1. If the recipient is active on the network, the message will be sent immediately, and you will be notified whether the message was successfully sent. 
    2. If the user is inactive, the message will be queued for their viewing when they sign back in. 
   
If the recipient username does not exist in the network, you will be prompted with sending a new command. 
<br/><br/>

#### Removing Account: 
To remove your account from the network, type the command "remove". This will remove your account and disconnect you from the network. 





