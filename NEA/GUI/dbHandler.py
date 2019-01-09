'''
[:] File: dbHandler.py
[:] Function: Communicate to the SQL Database and validate information
[:] Author: Harry Hegarty
[:] NEA Information:
	[Center Number]: 52221
	[Candidate Number]: 4062
'''

import loginHandler

try:
    import MySQLdb
    debug_mySql = True
except ImportError:
    import sys
    debug_mySql = False

def requestUser(attUsername):
	connect = sql.connect("23.91.70.146", "housesta_harry", "q;wX!d_Ukjo7", "housesta_csnea")
	ccur = connect.cursor()
	ccur.execute("SELECT password FROM users WHERE username = '%s'" % (attUsername))
	dbPassword = ccur.fetchall()
	connect.close
	dbPassword = str(dbPassword)
	dbPassword = ''.join(c for c in dbPassword if c not in "(,)'")
	return dbPassword

def checkUserAvail(dataUs,dataEm):
	connect = sql.connect("23.91.70.146", "housesta_harry", "q;wX!d_Ukjo7", "housesta_csnea")
	ccur = connect.cursor()
	ccur.execute("SELECT fullname FROM users WHERE username = '%s'" % (dataUs))
	dataResultUsr = ccur.fetchall()
	ccur.execute("SELECT fullname FROM users WHERE email = '%s'" % (dataEm))
	dataResultEm = ccur.fetchall()
	connect.close
	dataResultUsr = str(dataResultUsr)
	dataResultEm = str (dataResultEm)
	return dataResultUsr, dataResultEm

def insertUser(usrVar, pswVar, fnVar, emVar):
	connect = sql.connect("23.91.70.146", "housesta_harry", "q;wX!d_Ukjo7", "housesta_csnea")
	ccur = connect.cursor()
	sqlQ = ("INSERT INTO users (username,password,fullname,email) VALUES (%s,%s,%s,%s)" % (usrVar, pswVar, fnVar, emVar))
	ccur.execute(sqlQ)
	connect.commit()
	connect.close
