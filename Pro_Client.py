#!/usr/bin/python3

#This is Client side of FTP Protocol Socket Programming
#which is Client want send the file to the Server
#and Client receive reply from the Server

import socket			#Import socket module
import sys			#Import sys module
import os			#Import os module
from Crypto.Cipher import AES	#Import encryption module

#Encryption process
def encryption(decrypted_data):
	obj = AES.new(b"1234567891234567", AES.MODE_CFB, b"7654321987654321")
	encrypted_data = obj.encrypt(decrypted_data)

	return encrypted_data

#The IP Address or hostname of the server
ServerIP = "192.168.1.7"

#Create the Client socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Set the port
PORT = 8000

#Connect to the IP Address of server and print the output if connect.
s.connect((ServerIP, PORT))
print("\n[+]Connected to the Server: " + str(ServerIP))

#Print for which file want to send to the server
print("\n[+]Which File do you want to send? ")

#Enter the name of file that want to send
FILE = input("\n[+]Enter the File name send to server: ")
print("\n[+]Filename: " + FILE)

#Open a file for both reading and writing
file = open(FILE, "rb")	
SendData = file.read(1024)

#Sending filename to server
s.send(FILE.encode("utf-8"))

#This is for padding
length = 16 - (len(SendData) % 16)
SendData += bytes([length])*length

#Send data encrypted from Client to Server to decryt
SendData = encryption(SendData)

#Send data in while loop
while SendData:

	#Receive message or reply from the Server
	print("\n[+]Received Message from server: ", s.recv(1024).decode("utf-8"))

	s.send(SendData)

	SendData = file.read(1024)

	#Encrypt the File
	SendData = encryption(SendData)

#Close the Client connection
s.close()
print("\n[+]File has be send successfully!!! \n" )


