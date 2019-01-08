#File: main.py
#Author: Harry Hegarty
#For: Burnham Grammar School : CS NEA
#Task 2
#Description: Handles main tasks given by the user.

import credentialsHandler as creds

def credentialsHandler_export(exported_usrnm, exported_pswrd):
	imported_usrnm = exported_usrnm
	imported_pswrd = exported_pswrd
	creds.credentialsHandler_init(imported_usrnm, imported_pswrd)

exported_usrnm = input("Enter Username: ")
exported_pswrd = input("Enter Password: ")

credentialsHandler_export(exported_usrnm, exported_pswrd)