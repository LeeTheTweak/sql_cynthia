import mysql.connector

# Add a function for user to enter host, user, and password of connection.------------
askForConnection = "Connect to your database:"
hostname = input("Host: ")
username = input("Username: ")
password = input("Password: ")

# VARIABLES
mydb = mysql.connector.connect(host=hostname, user=username, passwd=password)
mycursor = mydb.cursor()

question = """\n
Type a number to execute a command
1 - Create Database, 2 - Use ~'db name'~, 3 - Show Databases, 4 - Exit
"""
askTables = """\n
1 - SHOW TABLES, 2 - SHOW DATABASES, 3 - Exit
"""

# FUNCTIONS


def showDatabases():
	presentDB = "\nHere are your current databases."
	print(presentDB.upper())
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)


def quit():
	mycursor("quit")


def ask():
	choice = input(question.upper())
	if choice == "1":
		askDBName = "What is the name of your new database?"
		dbName = input(askDBName.upper())
		mycursor.execute("CREATE DATABASE " + dbName)
		print(dbName + " is now a database!")
		ask()

	elif choice == "2":
		whichToUse = "Which database to use?"
		nowUsing = "You're now using, "

		dbUse = input(whichToUse.upper())
		mycursor.execute("USE " + dbUse)

		print(nowUsing + dbUse.upper())
		usingQuestions = input(askTables)

		if usingQuestions == "1":
			mycursor.execute("SHOW TABLES")
			for x in mycursor:
				print(x)
			ask()

		elif usingQuestions == "2":
			showDatabases()
			ask()

		elif usingQuestions == "3":
			quit()

	elif choice == "3":
		showDatabases()
		ask()

	elif choice == "4":
		quit()


showDatabases()
ask()

