import registerUserGUI
import dbHandler
import json
import hashlib

def newUser(usrVar, pswVar, confPswVar, fnVar, emVar):
	print(usrVar, pswVar, confPswVar, fnVar, emVar)
	
	usrVar = (json.dumps(usrVar))
	fnVar = (json.dumps(fnVar))
	emVar = (json.dumps(emVar))

	usrInfo = [usrVar, pswVar, confPswVar, fnVar, emVar]

	for x in usrInfo:
		print(x)


	dataUs = usrVar
	dataEm = emVar
	dataResultUsr, dataResultEm = dbHandler.checkUserAvail(dataUs,dataEm)
	dataResultUsr = ''.join(c for c in dataResultUsr if c not in "(),")
	dataResultEm = ''.join(c for c in dataResultEm if c not in "(),")

	print(dataResultEm, dataResultUsr)
	if (dataResultUsr == "" and dataResultEm == ""):
		print("alright")
		if (confPswVar == pswVar):
			attPasswordHashed = hashlib.sha256((pswVar).encode('utf-8')).hexdigest()
			print(attPasswordHashed)
			pswVar = attPasswordHashed
			pswVar = str(pswVar)
			pswVar = (json.dumps(pswVar))
			insertConf = dbHandler.insertUser(usrVar, pswVar, fnVar, emVar)
			print("now we go register page saying user created and then go back to login")
		else:
			print("wrong pw mate again reguister gui xx")
	else:
		print("error wrong  mate go back to register gui and mess around with text and styff")
