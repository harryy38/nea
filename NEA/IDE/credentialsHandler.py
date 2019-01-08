#File: credntialsHandler.pytring python
#Author: Harry Hegarty
#For: Burnham Grammar School : CS NEA
#Task 2
#Description: Handles every credential passed through the application

#___Imports
import uuid
import hashlib
import dbHandler
import encryptionHandler as encrypt

def credentialsHandler_encryptPass(creds_usrnm,creds_pswrd):
	encryptionHandler_saltRanGen = uuid.uuid4().hex #Uses UUID to generate a random number to salt our password
	encryptionHandler_hashedEntry = hashlib.sha256(encryptionHandler_saltRanGen.encode() + creds_pswrd.encode()).hexdigest() + ':' + encryptionHandler_saltRanGen #Encrypts the salt, adds it to the password, then adds an unhashed salt at the end, this prevents dictionary attacks 
    #print(encryptionHandler_hashedEntry)
	creds_hashedPswrd = encryptionHandler_hashedEntry
	creds_pswrd = creds_hashedPswrd	
	dbHandler.dbHandler_insertUser(creds_usrnm, creds_pswrd)
	
def credentialsHandler_init(imported_usrnm, imported_pswrd):
	global creds_usrnm
	global creds_pswrd
	creds_usrnm = imported_usrnm
	creds_pswrd = imported_pswrd 
	#print(creds_usrnm)
	#print(creds_pswrd)
	credentialsHandler_encryptPass(creds_usrnm,creds_pswrd)

	
def credentialsHandler_requestCreds(creds_usrnm):
	dbHandler.dbHandler_requestUser(creds_usrnm)
	
def credentialsHandler_validation(dbHandler_requestResults):
	sqlHashedPswrd = dbHandler_requestResults
	sqlHashedPswrdStr = str(sqlHashedPswrd)
	''.join( c for c in sqlHashedPswrdStr if c not in '[(,)]\'' )
	print(sqlHashedPswrdStr)
	#validationPassword, 
	validation_deSalt = sqlHashedPswrdStr.split(':')
	#validation_deSalt = [x[:x.index(':')] if ':' in x else x for x in sqlHashedPswrd]
	print(validation_deSalt)
	sqlHashedPswrdStr = validation_deSalt
	validationPassword = hashlib.sha256(validation_deSalt.encode() + sqlHashedPswrdStr.encode()).hexdigest()
	print(validationPassword)
	
	
