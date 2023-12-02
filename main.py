import mysql.connector


def admin_consol():
    pass


def data_entry_consol():
    pass


def guest_consol():
    mLevelOneChoice = ''
    mLevelTwoChoice = ''
    mLevelThreeChoice = ''
    while True:
        print("~~~~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~~~~~")
        print("Please input the part of the database you're interested in veiwing")
        mLevelOneChoice = input("(1) Art Pieces \t (2) Artists \t (3) Exhibitions \t (0) To quit the program: ")
        print()
        print()

        #Art piece menu
        if mLevelOneChoice == '1':
            print("~~~~~~~~~~~~~~~~ ART PIECES ~~~~~~~~~~~~~~~~")
        while mLevelOneChoice == '1':
            print("Please input the kind of art pieces you're interested in veiwing")
            mLeveltwoChoice = input("(1) Paintings \t (2) Sculptures \t (3) Statues \t (4) Other \t (0) Go Up a Level: ")
            print()
            print()
            if mLeveltwoChoice == '0':
                break

        #Artists menu
        if mLevelOneChoice == '2':
            print("~~~~~~~~~~~~~~~~ ARTISTS ~~~~~~~~~~~~~~~~")
        while mLevelOneChoice == '2':
            print("Please input the part of the database you're interested in veiwing")
            mLeveltwoChoice = input("Please type the name of the artist you're interested in \t (0) Go Up a Level: ")
            print()
            print()
            if mLeveltwoChoice == '0':
                break

        #Exhibitions Menu
        if mLevelOneChoice == '3':
            print("~~~~~~~~~~~~~~~~ EXHIBITIONS ~~~~~~~~~~~~~~~~")
        while mLevelOneChoice == '3':
            print("Please input the part of the database you're interested in veiwing")
            mLeveltwoChoice = input("(1) Search Exhibitions by ID \t (2) Search Exhibitions by name \t (0) Go Up a Level: ")
            print()
            print()
            if mLeveltwoChoice == '0':
                break
        
        if mLevelOneChoice == '0':
            break






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

    #cnx = mysql.connector.connect(
        #host="127.0.0.1",
        #port=3306,
        #user= username,
        #password= password)    
    ### Get a cursor
    #cur = cnx.cursor()
    ### Execute a query
    #cur.execute("use olympicarchery")
    
    if selection == '1':
        admin_consol()
    elif selection == '2':
        data_entry_consol()
    else:
        guest_consol()

    print("Thanks for using the program")