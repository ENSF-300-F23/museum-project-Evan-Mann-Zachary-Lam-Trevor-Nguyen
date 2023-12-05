import mysql.connector
from GlobalFunctions import *
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

        cur.execute("select * from art_object;")
        print(200*'~')
        print("Art Objects before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Art Object')
        print(200*'~')

        selecting = True
        while selecting:
            ID_no = input("Please input the ID number of the art object: ")
            if ID_no in getCurArtIDs(cur):
                print("\nInvalid Input, Please input a new unique ID that is not already in the database\n")
            elif len(ID_no) != 9:
                print("Invalid input. Please input a 9 digit ID number")
            else:
                selecting = False

        Year_created = input("Please input the year the art object was created: ")
        while len(Year_created) != 4: Year_created = input("Invalid Input. Year must be 4 digits. Please input a new year: ")
        Title = input("Please input the title of the art object: ")
        while len(Title) > 40: Title= input("Invalid Input. title must be less than 26 characters. Please input a new title: ")
        Descr = input("Please input the description of the art object: ")
        while len(Descr) > 40: input("Invalid Input. Description must be less than 26 characters. Please input a new description: ")
        Origin = input("Please input the origin of the art object: ")
        while len(Origin) > 15: input("Invalid Input. Origin must be less than 21 characters. Please input a new origin: ")
        Epoch = input("Please input the epoch of the art object: ")
        while len(Epoch) > 15: input("Invalid Input. Epoch must be less than 15 characters. Please input a new epoch: ")

        selecting = True
        while selecting:
            Collection_type = input("Please input the collection type that the object resides in (borrowed or permanent): ")
            if ID_no in ['borrowed', 'permanent']:
                print("\nInvalid Input, Please input choice exactly as shown\n")
            else:
                selecting = False
        
        if Collection_type == 'permanent':
            objStatus = input("Please input the status of the object: ")
            cost = input('Please input the cost of the object: ')
            dateAqquired = input("Please input the date the object was put into the permanent collection (XXXX-XX-XX [year - month - day]): ")
            selecting = True
            while selecting:
                if dateAqquired.replace('-', '').isnumeric() and dateAqquired[5] == '-' and dateAqquired[8] == '-' and len(dateAqquired) == 10 and int(dateAqquired[2:4]) <= 12 and int(dateAqquired[8:]) <=31:
                    selecting = False
                else:
                    dateAqquired = input("Invalid date, please re enter the date the piece was aqquired: ")
            ternaryCommand = f"INSERT INTO PERMANENT_COLLECTION VALUES ('{ID_no}','{objStatus}','{cost}','{dateAqquired}');"


        if Collection_type == 'borrowed':
            
            selecting = True
            while selecting:
                collectionBorrowedFrom = input("Please input the collection the piece was borrowed from: ")

                if collectionBorrowedFrom not in getCurCollectionIDs(cur) and Artist_name != 'None':
                    print("\nInvalid Input, Please input a collection ID that is already in the database\n")
                
                else:
                    selecting = False

            dateBorrowed = input("Please input the date the object was borrowed on (XXXX-XX-XX [year - month - day]): ")
            dateReturned = input('Please input the date the object was returned on (XXXX-XX-XX [year - month - day]): ')
            selecting = True
            while selecting:
                if dateBorrowed.replace('-', '').isnumeric() and dateBorrowed[5] == '-' and dateBorrowed[8] == '-' and len(dateBorrowed) == 10 and int(dateBorrowed[2:4]) <= 12 and int(dateBorrowed[8:]) <=31:
                    selecting = False
                else:
                    dateBorrowed = input("Invalid date, please re enter the date the piece was borrowed: ")            


            selecting = True
            while selecting:
                if dateReturned.replace('-', '').isnumeric() and dateReturned[5] == '-' and dateReturned[8] == '-' and len(dateReturned) == 10 and int(dateReturned[2:4]) <= 12 and int(dateReturned[8:]) <=31:
                    selecting = False
                else:
                    dateReturned = input("Invalid date, please re enter the date the piece was returned: ")
            ternaryCommand = f"INSERT INTO BORROWED VALUES ('{ID_no}','{objStatus}','{cost}','{dateAqquired}');"
        
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
            elif (i == '4'):
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
            if Artist_name not in getCurArtistNames(cur) and Artist_name != 'None':
                print("\nInvalid Input, Please input an artist name that is already in the database\n")
            elif len(Artist_name) > 30:
                print("\nInvalid Input. Artist name must be less than 20 characters")
            
            else:
                selecting = False

        art_obj_command = f"INSERT INTO ART_OBJECT VALUES ('{ID_no}','{Year_created}','{Title}','{Descr}','{Origin}','{Epoch}','{Collection_type}','{objType}','{Artist_name}');"
        cur.execute(art_obj_command)
        cur.execute(secondary_Command)
        

        cur.execute("select * from art_object;")
        print(200*'~')
        print("Art Objects after insert")
        print()
        printData(cur.column_names, cur.fetchall(), 'Art Object')
        print(200*'~')

        print()
        showArtTypeChanges = input(f"{objType} has had an insert as well, would you like to see those changes? (Y or N): ")
        while showArtTypeChanges not in ['Y','N']:  showArtTypeChanges = input('Invalid input. (Y or N): ')
        if showArtTypeChanges == 'Y':
            cur.execute(f"select * from {objType};")
            print(200*'~')
            print(f"{objType} after insert")
            print()
            printData(cur.column_names, cur.fetchall())
            print(200*'~')





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