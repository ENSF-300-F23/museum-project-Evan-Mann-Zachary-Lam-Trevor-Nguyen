import mysql.connector

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password= '33104001SqL?') #Input local system password


# Get a cursor
cur = cnx.cursor()

fd = open('sql_scripts\museum_db_initialization_WC.sql', 'r')
sqlFile = fd.read()
fd.close()
sqlCommands = sqlFile.split(';')

msg = IOError
for command in sqlCommands:
    try:
        if command.strip() != '':
            cur.execute(command)
    except (IOError, msg):
        print("Command skipped: ", msg)