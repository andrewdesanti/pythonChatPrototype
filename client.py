#importing packages necessary for TCP use and the threading of sending and recieving
import threading
import socket

#which IP and port are you connecting to? What is your desired nickname?
hostIP = str(input("HostIP? : "))
port = int(input("Port Number? : "))
nickname = input("Choose your nickname for this session: ")

#set up this socket instance as a client, begin connection with desired Ip and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((hostIP, port))

#print recieved messages in light purple to distinguish them from your own inputs
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 

#handles the recieving of messages from the server
def recieveing():
	while True:
		try:
			#upon the reciept of a message if it is 'Nickname' send input nickname, if it is just another message print it in light purple 
			message = client.recv(1024).decode('ascii')
			if message == 'Nickname':
				client.send(nickname.encode('ascii'))
			else:
				prLightPurple(message)
		except:
			#if an error occurs print an error and disconnect from the server
			print("ERROR")
			client.close()
			break

#handles the writing and sending of a message to the server
def writing():
	while True:
		#input the message, send it along with the nickname
		message = '{}: {}'.format(nickname, input(''))
		client.send(message.encode('ascii'))

#thread the recieving and sending so they can be ran parallel to eachother
recieveThread = threading.Thread(target = recieveing)
recieveThread.start()
writeThread = threading.Thread(target = writing)
writeThread.start()