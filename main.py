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
    print("What kind of action would you like to do")
    selecting = True
    while selecting:
        s = input("(1) Insert \t (2) Update \t (3) Delete: ")
        if (s == '1'):
            actionType = "INSERT"
            selecting = False
        elif (s == '2'):
            actionType = "UPDATE"
            selecting = False
        elif (s == '3'):
            actionType = "DELETE"
            selecting = False
        else:
            print("Invalid input")
            print()

    if (actionType == "INSERT"):
        ID_no = input("Please input the ID number of the art object: ")
        Year_created = input("Please input the year the art object was created: ")
        Title = input("Please input the title of the art object: ")
        Descr = input("Please input the description of the art object: ")
        Origin = input("Please input the origin of the art object: ")
        Epoch = input("Please input the epoch of the art object: ")
        Collection_type = input("Please input the collection type that the object resides in: ")
        print("What kind of art object are you inserting")
        
        selecting = True
        while selecting:
            i = input("(1) Painting \t (2) Statue \t (3) Sculpture \t (4) Other: ")
            if (i == '1'):
                objType = "Painting"
                paint_type = input("Please input the paint type: ")
                Drawn_on = input("Please input the medium the painting is drawn on: ")
                style = input("Please input the style of the painting: ")
                selecting = False
            elif (i == '2'):
                objType = "Statue"
                material = input("Please input the material the statue is made out of: ")
                height = input("Please input the height of the statue: ")
                weight = input("Please input the weight of the statue: ")
                style = input("Please input the style of the statue: ")
                selecting = False
            elif (i == '3'):
                objType = "Sculpture"
                material = input("Please input the material the sculpture is made out of: ")
                height = input("Please input the height of the sculpture: ")
                weight = input("Please input the weight of the sculpture: ")
                style = input("Please input the style of the sculpture: ")
                selecting = False
            elif (i == '3'):
                objType = "Other"
                other_type = input("Please input the type of this object: ")
                style = input("Please input this objects style: ")
                selecting = False
            else:
                print("Invalid input")
                print()
        Artist_name = input("Please input the name of the artist who created the art object: ")
        #COMPLETE SQL COMMAND CREATION AND EXECUTION

    if (actionType == "UPDATE"):
        print("What are you updating")
        selecting = True
        while selecting:
            i = input("(1) Art Object \t (2) Painting \t (3) Statue \t (4) Sculpture \t (5) Other: ")
            #if (i == '1'):

            #elif (i == '2'):

            #elif (i == '3'):

            #elif (i == '4'):

            #elif (i == '5'):

            #else:
                #print("Invalid input")
                #print()


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



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def admin_console():
    pass


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
            editArtObj(cur)
            break
        #Artists menu
        while mLevelOneChoice == '2':
            editArtists(cur)
            break

        #Permanent Collection menu
        while mLevelOneChoice == '3':
            editPermCollection(cur)
            break

        #Borrowed Collection menu
        while mLevelOneChoice == '4':
            editBorrowCollection(cur)
            break

        #Exhibitions menu
        while mLevelOneChoice == '5':
            editExhibitions(cur)
            break

        #Seperate Collections menu
        while mLevelOneChoice == '6':  
            editSepCollections(cur)
            break


        if mLevelOneChoice == '0':
            break
        else:
            print("Invalid Option")
            print()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




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