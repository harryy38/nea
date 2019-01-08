#File: encryptionHandler.py
#Author: Harry Hegarty
#For: Burnham Grammar School : CS NEA
#Task 2
#Description: Handles hashing and salting of passwords

#___Imports
import uuid
import hashlib

def encryptionHandler_hash(creds_pswrd):
	encryptionHandler_saltRanGen = uuid.uuid4().hex #Uses UUID to generate a random number to salt our password
	encryptionHandler_hashedEntry = hashlib.sha256(encryptionHandler_saltRanGen.encode() + creds_pswrd.encode()).hexdigest() + ':' + encryptionHandler_saltRanGen #Encrypts the salt, adds it to the password, then adds an unhashed salt at the end, this prevents dictionary attacks 
	return encryptionHandler_hashedEntry
	
#def encryptionHandler_checkHash()