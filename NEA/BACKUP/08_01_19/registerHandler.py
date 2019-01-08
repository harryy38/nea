import registerUserGUI
import dbHandler
import json

def newUser(usrVar, pswVar, confPswVar, fnVar, emVar):
	print(usrVar, pswVar, confPswVar, fnVar, emVar)
	
	usrVar = (json.dumps(usrVar))
	pswVar = (json.dumps(pswVar))
	confPswVar = (json.dumps(confPswVar))
	fnVar = (json.dumps(fnVar))
	emVar = (json.dumps(emVar))
	##emVar = emVar.replace("@", "//AND//")

	usrInfo = [usrVar, pswVar, confPswVar, fnVar, emVar]

	for x in usrInfo:
		print(x)
	#usrInfo = 
	#for x in usrInfo:
	#	x = ("\"" + x + "\"")
	#	print(x)


	dataUs = usrVar
	dataEm = emVar
	dataResultUsr, dataResultEm = dbHandler.checkUserAvail(dataUs,dataEm)
	dataResultUsr = ''.join(c for c in dataResultUsr if c not in "(),")
	dataResultEm = ''.join(c for c in dataResultEm if c not in "(),")

	print(dataResultEm)
	if (dataResultUsr == "" and dataResultEm == ""):
		print("alright")
		if (confPswVar == pswVar):
			insertConf = dbHandler.insertUser(usrVar, pswVar, fnVar, emVar)
			print("now we go register page saying user created and then go back to login")
		else:
			print("wrong pw mate again reguister gui xx")
	else:
		print("error wrong shit mate go back to register gui and mess around with text and styff")
	#if (dataResultUsr != ""):
	#	registerUserGUI.userInvalid()
	#elif (dataResultUsr == ""):

	#print(dataResultUsr, dataResultEm)
'''
	if (dataResult == ""):
		
	else
		return "errorUserDupe"
	#pass conf
	if (pswVar == confPswVar):
		print("right")
	else:
		return "errorConfPW"
		'''