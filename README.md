# pythonChatPrototype
Andrew DeSanti's Python LAN Chat Prototype for CPE490 Fall 2020. A Client-Server chatroom capable of sending messages to a group of clients in a single room.  
## Install
`git clone https://github.com/jagerking/pythonChatPrototype.git`
### To Run as a Server:
```
{
$ cd pythonChatPrototype 
$ python3 server.py
}
```
### To Run as a Client:
```
{
$ cd pythonChatPrototype 
$ python3 client.py
}
```
## Server Use:
On runtime you will be asked to provide an IP address. This can be easily found with the Linux command `ifconfig` labeled as `inet` in the format `xxx.xxx.xxx.xxx`, a port number between 0 and 65535, and a message of the day blurb. Once entered the server will begin listening for connecting clients. Upon the conncetion of a client, you will be given an alert containing the the IP and Port the client connected from, as well as their chosen nickname. All messages sent between clients can be seen in purple on the server. 
## Client Use:
### Connecting:
On runtime you will be asked to provide the server's IP address and port number along with a chosen nickname for the session. Upon a successful connection, the server will send the new client a confirmation messages containing their nickname as well as a list of commands. The client can then type a message to be sent to the server as well as all connected clients. Keep in mind a client will recieve their own messages and all recieved messages will be colored purple. 
### Commands:
There are several commands available for the clients to use. Keep in mind the server's response to these commands will be visable to all connected clients.
-!clients : This command sends a list of all currently connected client Nicknames
-!about : This command sends a short blurb about the chatroom and a link to this GitHub page.
-!motd: This command sends the Message of the Day provided by the server at its start.