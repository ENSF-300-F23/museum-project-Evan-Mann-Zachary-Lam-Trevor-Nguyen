import mysql.connector
from GetterFunctions import *
from GuestUserFunctions import *
from AdminUserFunctions import *


#Data entry user input/delete functions
def editArtObj(cur, actionType = None):
    print("What kind of action would you like to do")
    while actionType == None:
        s = input("(1) Insert \t (2) Update \t (3) Delete: ")
        if (s == '1'):
            actionType = "INSERT"
        elif (s == '2'):
            actionType = "UPDATE"
        elif (s == '3'):
            actionType = "DELETE"
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
                secondary_Command = f"INSERT INTO PAINTING VALUES ('{ID_no}','{paint_type}','{Drawn_on}','{style}');"
                selecting = False
            elif (i == '2'):
                objType = "Statue"
                material = input("Please input the material the statue is made out of: ")
                height = input("Please input the height of the statue: ")
                weight = input("Please input the weight of the statue: ")
                style = input("Please input the style of the statue: ")
                secondary_Command = f"INSERT INTO STATUE VALUES ('{ID_no}','{material}','{height}','{weight}','{style}');"
                selecting = False
            elif (i == '3'):
                objType = "Sculpture"
                material = input("Please input the material the sculpture is made out of: ")
                height = input("Please input the height of the sculpture: ")
                weight = input("Please input the weight of the sculpture: ")
                style = input("Please input the style of the sculpture: ")
                secondary_Command = f"INSERT INTO SCULPTURE VALUES ('{ID_no}','{material}','{height}','{weight}','{style}');"
                selecting = False
            elif (i == '3'):
                objType = "Other"
                other_type = input("Please input the type of this object: ")
                style = input("Please input this objects style: ")
                secondary_Command = f"INSERT INTO OTHER VALUES ('{ID_no}','{other_type}','{style}');"
                selecting = False
            else:
                print("Invalid input")
                print()
            
            selecting = True
            while selecting:
                Artist_name = input("Please input the name of the artist who created the art object: ")
                if Artist_name not in getCurArtistNames(cur):
                    print("\nInvalid Input, Please input an artist name that is already in the database\n")
                else:
                    selecting = False

        art_obj_command = f"INSERT INTO ART_OBJECT VALUES ('{ID_no}','{Year_created}','{Title}','{Descr}','{Origin}','{Epoch}','{Collection_type}','{objType}','{Artist_name}');"
        cur.execute(art_obj_command)
        cur.execute(secondary_Command)
        
        cur.execute("select * from art_object;")
        test = cur.fetchall()
        print()


    if (actionType == "UPDATE"):
        print("What are you updating")
        selecting = True
        while selecting:
            i = input("(1) Art Object \t (2) Painting \t (3) Statue \t (4) Sculpture \t (5) Other: ")
            if (i == '1'):
                test = input("Do you want to edit the artist? Y or N")
                if (test == 'Y'):
                    editArtists(cur, "UPDATE")
            #elif (i == '2'):

            #elif (i == '3'):

            #elif (i == '4'):

            #elif (i == '5'):

            #else:
                #print("Invalid input")
                #print()


def editArtists(cur, actionType = None):
    if actionType == None:
        print("What kind of action would you like to do")
    while actionType == None:
        s = input("(1) Insert \t (2) Update \t (3) Delete: ")
        if (s == '1'):
            actionType = "INSERT"
        elif (s == '2'):
            actionType = "UPDATE"
        elif (s == '3'):
            actionType = "DELETE"
        else:
            print("Invalid input")
    print(f"Edit artists with {actionType} called")


def editPermCollection(cur, actionType = None):
    if actionType == None:
        print("What kind of action would you like to do")
    while actionType == None:
        s = input("(1) Insert \t (2) Update \t (3) Delete: ")
        if (s == '1'):
            actionType = "INSERT"
        elif (s == '2'):
            actionType = "UPDATE"
        elif (s == '3'):
            actionType = "DELETE"
        else:
            print("Invalid input")
            print()


def editBorrowCollection(cur, actionType = None):
    if actionType == None:
        print("What kind of action would you like to do")
    while actionType == None:
        s = input("(1) Insert \t (2) Update \t (3) Delete: ")
        if (s == '1'):
            actionType = "INSERT"
        elif (s == '2'):
            actionType = "UPDATE"
        elif (s == '3'):
            actionType = "DELETE"
        else:
            print("Invalid input")
            print()


def editExhibitions(cur, actionType = None):
    if actionType == None:
        print("What kind of action would you like to do")
    while actionType == None:
        s = input("(1) Insert \t (2) Update \t (3) Delete: ")
        if (s == '1'):
            actionType = "INSERT"
        elif (s == '2'):
            actionType = "UPDATE"
        elif (s == '3'):
            actionType = "DELETE"
        else:
            print("Invalid input")
            print()


def editSepCollections(cur, actionType = None):
    if actionType == None:
        print("What kind of action would you like to do")
    while actionType == None:
        s = input("(1) Insert \t (2) Update \t (3) Delete: ")
        if (s == '1'):
            actionType = "INSERT"
        elif (s == '2'):
            actionType = "UPDATE"
        elif (s == '3'):
            actionType = "DELETE"
        else:
            print("Invalid input")
            print()






#Data entry console
def data_entry_console(cur):
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
        elif mLevelOneChoice not in ['0','1','2','3','4','5','6']:
            print("Invalid Option")
            print()