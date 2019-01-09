'''
[:] File: loginHandler.py
[:] Function: Deal with registered users logging into the program
[:] Author: Harry Hegarty
[:] NEA Information:
	[Center Number]: 52221
	[Candidate Number]: 4062
'''

import dbHandler
import loginGui
import hashlib

def importVars(userVar, passVar):
	attUsername = userVar
	attPassword = passVar
	dbPassword = dbHandler.requestUser(attUsername)
	username = attUsername
	attPasswordHashed = hashlib.md5(attPassword.encode())
	if (attPasswordHashed == dbPassword):
		madDiceGameGUI.vp_start_gui()
	else:
		exceptionType = "incorrect_pw"
		loginGui.incorrectInfo(exceptionType)
