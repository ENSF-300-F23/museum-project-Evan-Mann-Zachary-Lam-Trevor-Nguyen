import mysql.connector

#Guest user search functions
def searchArtObjects(searchItem, cursor):
    instr = ""
    join = ""

    showArtists = input("Do you want to see the artist who created each piece as well? (Y  or N): ")
    showCollection = input("Do you want to see the collection each piece comes from (Y or N): ")
    showDetailedInfo = input("Would you like extra details such as the pieces origin or epoch (Y or N): ")

def searchArtists(searchItem, cursor):
    instr = ""
    join = ""

    if searchItem == "Name":
        artistName = input("Please input the artists name you're interested in: ")
        showPiecesToo = input("Would you like to see the pieces this artist created? (Y or N): ") # this could come after the artist info is printed to the screen instead

    elif searchItem == "Epoch":
        artistEpoch = input("Please input the epoch of the artist you're interested in: ")

    elif searchItem == "All":
        print()


    # This should print 

def searchExhibitions(searchItem, cursor):
    instr = ""
    join = ""

    if searchItem == "ID":
        artistName = input("Please input the ID of the exhibit you're interested in: ")
        
    elif searchItem == "Name":
        artistEpoch = input("Please input the name of the exhibit you're interested in: ")


#Data entry user input/delete functions
def editArtObj(cursor):
    pass
def editArtists(cursor):
    pass
def editPermCollection(cursor):
    pass
def editBorrowCollection(cursor):
    pass
def editExhibitions(cursor):
    pass
def editSepCollections(cursor):
    pass


#Admin functions




def admin_console():
    pass


def data_entry_console():
    mLevelOneChoice = ''
    while True:
        print("~~~~~~~~~~~~~~~~ Database Search ~~~~~~~~~~~~~~~~")
        print("Please choose the part of the data base you wish to view")
        print("(1) Art Objects \t (2) Artists \t\t\t (3) Permanent Collection \t (4) Borrowed Collection")
        mLevelOneChoice = input("(5) Exhibitions \t (6) Seperate Collections \t (0) Quit the Program : ")
        print()
        print()

        #Art Objects menu
        while mLevelOneChoice == '1':
            editArtObj()
            break
        #Artists menu
        while mLevelOneChoice == '2':
            editArtists()
            break

        #Permanent Collection menu
        while mLevelOneChoice == '3':
            editPermCollection()
            break

        #Borrowed Collection menu
        while mLevelOneChoice == '4':
            editBorrowCollection()
            break

        #Exhibitions menu
        while mLevelOneChoice == '5':
            editExhibitions()
            break

        #Seperate Collections menu
        while mLevelOneChoice == '6':  
            editSepCollections()
            break


        if mLevelOneChoice == '0':
            break
        else:
            print("Invalid Option")
            print()






def guest_console():
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
        while mLevelOneChoice == '1':
            print("~~~~~~~~~~~~~~~~ ART PIECES ~~~~~~~~~~~~~~~~")
            print("Please input the kind of art pieces you're interested in veiwing")
            mLevelTwoChoice = input("(1) Paintings \t (2) Sculptures \t (3) Statues \t (4) Other \t (0) Go Up a Level: ")
            print()
            print()

            if mLevelTwoChoice == '1':
                searchArtObjects("Paintings", cur)
            elif mLevelTwoChoice == '2':
                searchArtObjects("Sculptures", cur)
            elif mLevelTwoChoice == '3':
                searchArtObjects("Statues", cur)
            elif mLevelTwoChoice == '4':
                searchArtObjects("Other", cur)
            elif mLevelTwoChoice == '0':
                break
            else:
                print("Invalid Option")
                print()



        #Artists menu 
        while mLevelOneChoice == '2':
            print("~~~~~~~~~~~~~~~~ ARTISTS ~~~~~~~~~~~~~~~~")
            print("Please input the part of the database you're interested in veiwing")
            mLevelTwoChoice = input("(1) Search Artist by Name \t (2) Search Artist by epoch \t (3) See a list of all artists \t (0) Go Up a Level: ")
            print()
            print()

            if mLevelTwoChoice == '1':
                searchArtists("Name", cur)
            elif mLevelTwoChoice == '2':
                searchArtists("Epoch", cur)
            elif mLevelTwoChoice == '3':
                searchArtists("All", cur)
            elif mLevelTwoChoice == '0':
                break
            else:
                print("Invalid Option")
                print()



        #Exhibitions Menu
        while mLevelOneChoice == '3':
            print("~~~~~~~~~~~~~~~~ EXHIBITIONS ~~~~~~~~~~~~~~~~")
            print("Please input the part of the database you're interested in veiwing")
            mLevelTwoChoice = input("(1) Search Exhibitions by ID \t (2) Search Exhibitions by name \t (0) Go Up a Level: ")
            print()
            print()
            
            if mLevelTwoChoice == '1':
                searchExhibitions("ID", cur)
            elif mLevelTwoChoice == '2':
                searchExhibitions("Name",cur)
            elif mLevelTwoChoice == '0':
                break
            else:
                print("Invalid Option")
                print()
        


        if mLevelOneChoice == '0':
            break
        else:
            print("Invalid Option")
            print()






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
    ### Get a cursor
    cur = cnx.cursor()
    ### Execute a query
    cur.execute("USE MUSEUM;")
    
    if selection == '1':
        admin_console()
    elif selection == '2':
        data_entry_console()
    else:
        guest_console()

    print("Thanks for using the program")