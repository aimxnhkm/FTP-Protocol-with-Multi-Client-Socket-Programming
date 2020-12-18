#!/usr/bin/python3

#This is Server side of FTP Protocol Socket Programming
#which is Server received and stored the file send from the Client
#and Server send reply to the Client

import socket				#Import the socket library
import os				#Import os library
import sys, errno			#Import sys library
from _thread import*			#Import the thread module
from Crypto.Cipher import AES		#Import encryption library

#For decryption process
def decrypt(encrypted_data):
	obj = AES.new(b"1234567891234567", AES.MODE_CFB, b"7654321987654321")
	decrypted_data = obj.decrypt(encrypted_data)

	return decrypted_data


#Create the Server socket
#TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("\n[+]Socket successfully created \n")


#Server Port
PORT = 8000


#Define ThreadCount to zero
ThreadCount= 0


#Bind the socket to local address
s.bind(('', PORT))
print("[+]Socket binded to " + str(PORT))


#Enabling the server to accept connections
#5 here is the number of unaccepted connection that
#the system will allow before refusing new connections
s.listen(5)
print("\n[+]Waiting for the connection...")


print("\n-------------------------------------------------------------------------")


#Define threaded_client for received the data from Client
def threaded_client(connection):

	#Send reply to the client
	connection.send(str.encode("\n\n          |--------------------------------------|\n          |             FTP PROTOCOL             |\n          |--------------------------------------|\n          |  Hi Client [IP Address: " + addr[0] + "],| \n          |         WELCOME TO THE SERVER        |\n          |--------------------------------------|\n          |              THANK YOU!!             |\n          |--------------------------------------|"))

	#A forever loop until we interrupt it or an error occurs
	while True:
		#Receive filename connection
		Filename = connection.recv(1024)
		#Open a file for writing only
		file = open("Filename", 'wb')

		RecvData = conn.recv(1024)
		RecvData = decrypt(RecvData)

		while RecvData:
			file.write(RecvData)
			RecvData = connection.recv(1024)
			#Decrypt the File
			RecvData = decrypt(RecvData)

		break

	#Close the file and print the output
	file.close()
	print("\n[+]File has been copied and stored successfully")

	#Close connection and print the output
	connection.close()
	print("\n[+]Server close the connection")

	print("\n------------------------------------------------------------------------ \n")

#A forever loop
while True:
	#Accept Client's connection
	conn, addr = s.accept()

	#Print connected to the Client IP Adress
	print("\n[+]Connected to: " + addr[0] + ":" + str(addr[1]))

	#Thread function
	start_new_thread(threaded_client,(conn, ))

	#Thread looping
	ThreadCount += 1

	#Print the number of thread
	print("\n[+]Thread Number: " + str(ThreadCount))

#Close connection
s.close()

