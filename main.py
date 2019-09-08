import mysql.connector

# Add a function for user to enter host, user, and password of connection.------------
greetings = "\nHello there! I'm Cynthia and I'll be here to help you out!"			# GREETING
askForConnection = "Connect to your database:\n"									# ASK TO CONNECT

print(greetings.upper())															# GREETS AND ASKS USER TO CONNECT TO HIS OR HER DATABASE.
print(askForConnection.upper())

hostname = input("Host: ")
username = input("Username: ")
password = input("Password: ")

# VARIABLES
mydb = mysql.connector.connect(host=hostname, user=username, passwd=password)		# DATABASE CREDENTIALS INPUTS.
mycursor = mydb.cursor()

############################################# MAIN FUNCTION PROMPTS ############################################

whats_db_name = "What is the name of your new database?\n"

question = """\n
Type a number to execute a command
1 - CREATE DATABASE, 2 - Use ~'db name'~, 3 - SHOW DATABASES, 4 - DELETE DATABASE, 5 - EXIT
"""

askTables = """\n
1 - SHOW TABLES, 2 - SHOW DATABASES, 3 - EXIT
"""

describeLobby = """
1 - REVEAL TABLE, 2 - SHOW DATABASES, 3 - EXIT
"""

presentDB = "\nHere are your current databases."

whichToUse = "Which database to use?\n"

nowUsing = "You're now using, "

describeWhatStr = "What table do you want to reveal?:\n"

##################################################################################################




################################################################
# FUNCTIONS	OUTSIDE MAIN LOOP.								   #
################################################################

# FOR SHOWING DATABASES.

def showDatabases():
	print(presentDB.upper())
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:		# GETS THE WHOLE LIST OF DATABASES.
		print(x)

# FOR QUITTING SQL CYNTHIA

def quit():
	print("******************* GOOD BYE! *****************************\n\n\n")
	mycursor.execute("exit")

# FOR DELETING A DATABASE.

def delete_database():
	dropDB = input("Which database would you like to delete?\n")
	mycursor.execute("DROP DATABASE " + dropDB)

def describeTable(selectedTable):
	mycursor.execute("DESCRIBE " + selectedTable)
	for x in mycursor:
		print(x)

###################################################################


# THE MAIN FUNCTION OF THE PROGRAM. THIS FUNCTION SIMULATES A DO WHILE LOOP.

def ask():													# THE MAIN CHOICES LOOP
	choice = input(question.upper())
	if choice == "1":										# IN MAIN LOBBY, IF USER HITS 1, CREATE DATABASE TYPED. PRESENT MAIN LOBBY.
		askDBName = whats_db_name
		dbName = input(askDBName.upper())
		mycursor.execute("CREATE DATABASE " + dbName)
		print(dbName + " is now a database!")
		ask()

		

	elif choice == "2":										# IN MAIN LOBBY, IF USER HITS 2, USE DATABASE TYPED.
		dbUse = input(whichToUse.upper())
		mycursor.execute("USE " + dbUse)
		print(nowUsing + dbUse.upper())
		usingQuestions = input(askTables)



		if usingQuestions == "1":							# IN USING DATABASE SECTION, IF 1, SHOW TABLES IN DB. PRESENT MAIN LOBBY.
			mycursor.execute("SHOW TABLES")
			for x in mycursor:								# FOR LOOP FOR GETTING LIST OF TABLES.
				print(x)



			usingTableQuestions = input(describeLobby)  	# IN USING TABLE SECTION, IF 1, DESCRIBE A TABLE INPUTED.
			if usingTableQuestions == "1":
				tableTyped = input(describeWhatStr.upper())
				describeTable(tableTyped)



		elif usingQuestions == "2":							# IN USING DATABASE SECTION, IF 2, SHOW DATABASES. PRESENT MAIN LOBBY.
			showDatabases()
			ask()



		elif usingQuestions == "4":							# IN USING DATABASE SECTION, IF 4, QUIT PROGRAM.
			quit()



	elif choice == "3":										# IN MAIN LOBBY, IF 3, SHOW DATABASES. PRESENT MAIN LOBBY.
		showDatabases()
		ask()



	elif choice == "4":										# IN MAIN LOBBY, IF 4, DELETE DATABASE TYPED. PRESENT MAIN LOBBY.
		delete_database()
		ask()



	elif choice == "5":										# IN MAIN LOBBY, IF 5, QUIT PROGRAM.
		quit()


# CALLING THE THESE FUNCTIONS.

showDatabases()
ask()

