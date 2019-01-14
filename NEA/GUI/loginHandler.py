import dbHandler
import loginGui
import hashlib

def importVars(userVar, passVar):
	attUsername = userVar
	attPassword = passVar
	dbPassword = dbHandler.requestUser(attUsername)
	hAttPassword = hashlib.sha256((attPassword).encode('utf-8')).hexdigest()
	username = attUsername
	if (hAttPassword == dbPassword):
		putMainHereWhenIDoneItLoLOlOl
	else:
		exceptionType = "incorrect_pw"
		loginGui.incorrectInfo(exceptionType)
