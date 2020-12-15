#importing packages necessary for TCP use and the handling of multiple clients at once...
import socket
import threading

#ask user for server info that clients will use to connect...
hostIP = str(input("HostIP? : "))
port = int(input("Port Number? : "))
#ask for message of the day for the !motd command
motd = str(input("Message of the Day?: "))
tempMOTD = motd
#!about blurb
about = "This is a Python LAN chat server prototype for Andrew DeSanti's final for CPE490 Fall 2020. More info here: https://github.com/jagerking/pythonChatPrototype ."

#set this socket instance up as the server, claim IP and Port, begin listening to the correct port...
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hostIP, port))
server.listen()

#initialize lists that will contain client info and the corresponding nickname...
clientList = []
nicknameList = []

#print recieved messages in light purple to distinguish them
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 

#this function sends all recieved messages to all known clients...
def sending(message):
	for client in clientList:
		client.send(message)


#controls the sending of messages and the removal of clients...
def handling(client):
	while True:
		#if there is no error (e.g. client application has closed) send a recieved message...
		try:
			message = client.recv(1024)
			prLightPurple(message.decode('ascii'))
			commands(message)
			sending(message)



		#if an error has been thrown, remove the client and inform all other clients...
		except:
			index = clientList.index(client)
			clientList.remove(client)
			client.close()
			nickname = nicknameList[index]
			sending('{} has left!'.format(nickname).encode('ascii'))
			nicknameList.remove(nickname)
			break
#function that actively runs the server...
def recieving():
	while True:
		#upon the connection of a client, split the accepted client and info into two variables and print a connection notification to the terminal
		client, address = server.accept()
		print("Connected: {}".format(str(address)))

		#upon receiving a message 'Nickname', the client will then send the server back a nickname, store it in nicknameList[]
		client.send('Nickname'.encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknameList.append(nickname)
		clientList.append(client)

		#print nickname to terminal, send all other clients a new client notification, send the new client a joined notification
		print("Nickname: {}".format(nickname))
		sending("{} has joined \n".format(nickname).encode('ascii'))
		client.send('Connected to server \n Commands: !clients, !motd, !about'.encode('ascii'))

		#thread each client into its own itteration of the handling function so they may run parrallel to each other
		handlingThread = threading.Thread(target=handling, args=(client,))
		handlingThread.start()
#actually run the recieving function

def commands(encodedMessage):
	mess = encodedMessage.decode('ascii')
	tempNickStr = ""
	for j in nicknameList:
		if mess == j + ": !clients":
			tempNickStr = str(nicknameList)
			sending(tempNickStr.encode('ascii'))
		elif mess == j + ": !motd":
			sending(tempMOTD.encode('ascii'))
		elif mess == j + ": !about":
			sending(about.encode('ascii'))

recieving()
