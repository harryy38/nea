#File: dbHandler.py
#Author: Harry Hegarty
#For: Burnham Grammar School : CS NEA
#Task 2
#Description: Handles INSERTING & SELECTING SQL Queries

#___Imports
import MySQLdb as sql
import credentialsHandler as creds

def dbHandler_insertUser(creds_usrnm,creds_pswrd):
	connect = sql.connect("23.91.70.146", "housesta_harry", "q;wX!d_Ukjo7", "housesta_csnea")
	ccur = ccur.cursor()
	ccur.execute("INSERT INTO users (username,password) VALUES (?,?)", (creds_usrnm,creds_hashedPswrd))
	connect.commit()
	connect.close()

def dbHandler_requestUser(creds_usrnm):
	connect = sql.connect("database.db")
	handler = connect.cursor()
	handler.execute("SELECT password FROM users WHERE username = '%s'" % (creds_usrnm))
	dbHandler_requestResults = handler.fetchall()
	creds.credentialsHandler_validation(dbHandler_requestResults)
	connect.close()
	
