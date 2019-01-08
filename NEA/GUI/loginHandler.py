import dbHandler
import loginGui

def importVars(userVar, passVar):
	attUsername = userVar
	attPassword = passVar
	dbPassword = dbHandler.requestUser(attUsername)
	username = attUsername
	if (attPassword == dbPassword):
		putMainHereWhenIDoneItLoLOlOl
	else:
		exceptionType = "incorrect_pw"
		loginGui.incorrectInfo(exceptionType)
