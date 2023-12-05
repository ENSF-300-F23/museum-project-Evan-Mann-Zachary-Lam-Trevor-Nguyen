import mysql.connector
from GetterFunctions import *
from GuestUserFunctions import *
from DataEntryUserFunctions import *
from AdminUserFunctions import *



if __name__ == "__main__":
    #Inital setup
    print()
    print("~~~Welcome to the ENSF 300 Museum Database~~~")
    print()
    print("Please input your role from the following:\n(1) Database Admin\n(2) Data Entry\n(3) Browse as a Guest")
    while True:
        selection = input("Type 1, 2, or 3 for your selection: ")
        if selection not  in ['1','2','3']:
            print("Invalid Selection\n")
        else:
            break

    if selection in ['1', '2']:
        username = input("Username: ")
        password = input("Password: ")
    else:
        username = "guest"
        password = None

    print()
    #Uncomment once the database is complete and can actually be used for now this is just a placeholder till later

    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user= username,              
        password= password)   
    ### Get a cur
    cur = cnx.cursor()
    ### Execute a query
    cur.execute("USE MUSEUM;")


    if selection == '1':
        admin_console(cur)
    elif selection == '2':
        data_entry_console(cur)
    else:
        guest_console(cur)

    print("Thanks for using the program")