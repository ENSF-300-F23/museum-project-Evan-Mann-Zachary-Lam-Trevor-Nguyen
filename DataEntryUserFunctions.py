import mysql.connector
from GlobalFunctions import *
from GuestUserFunctions import *
from AdminUserFunctions import *


#Data entry user input/delete functions
def editArtObj(cur, actionType = None):
    #Asking the user what kind of action they would like to do on the art object tables
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
            print()
            print("Invalid input")
            print()
    
    #if that action was insert the following code block runs
    if (actionType == "INSERT"):

        #display the current state of the art_object table before changes
        cur.execute("select * from art_object;")
        print(200*'~')
        print("Art Objects before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Art Object')
        print(200*'~')

        #Getting the ID of the object and checking that it doesn't already exist in the database
        selecting = True
        while selecting:
            ID_no = input("Please input the ID number of the art object: ")
            if ID_no in getCurArtIDs(cur):
                print("\nInvalid Input, Please input a new unique ID that is not already in the database\n")
            elif len(ID_no) != 9:
                print("Invalid input. Please input a 9 digit ID number")
            else:
                selecting = False

        #Input the year and check its length (All lengths are checked in art obejct due to printing constraints since there are so many columns)
        Year_created = input("Please input the year the art object was created: ")
        while len(Year_created) != 4: Year_created = input("Invalid Input. Year must be 4 digits. Please input a new year: ")
        
        #Input the title and check its length
        Title = input("Please input the title of the art object: ")
        while len(Title) > 40: Title= input("Invalid Input. title must be less than 40 characters. Please input a new title: ")
        
        #Input the description and check its length
        Descr = input("Please input the description of the art object: ")
        while len(Descr) > 40: Descr = input("Invalid Input. Description must be less than 40 characters. Please input a new description: ")
        
        #Input the origin and check its length
        Origin = input("Please input the origin of the art object: ")
        while len(Origin) > 15: Origin = input("Invalid Input. Origin must be less than 15 characters. Please input a new origin: ")
        
        #Input the epoch and check its length
        Epoch = input("Please input the epoch of the art object: ")
        while len(Epoch) > 15: Epoch = input("Invalid Input. Epoch must be less than 15 characters. Please input a new epoch: ")

        #Input the collection and make sure it is either permanent or borrowed
        selecting = True
        while selecting:
            Collection_type = input("Please input the collection type that the object resides in (Borrowed or Permanent): ")
            if Collection_type not in ['Borrowed', 'Permanent']:
                print("\nInvalid input, please input choice exactly as shown\n")
            else:
                selecting = False
        
        #If the art object belongs to the permanent collection a new entry within that table must be created with a foreign key
        #pointing back to the Art object must be created. This code block walks the user through that process similarly to
        #What they had been doing up until this point
        if Collection_type == 'Permanent':
            #Inputting a new object status
            selecting = True
            while selecting:
                objStatus = input("Please input the status of the object (Displayed, Stored, Loaned): ")
                if objStatus not in ('Displayed', 'Stored', 'Loaned'):
                    print("Invalid input, please input Displayed, Stored or Loaned")
                else:
                    selecting = False
            
            selecting = True
            cost = input("Please input the cost of the art object: ")
            while selecting:
                selecting = False
                try:    
                    val = float(cost) 
                except ValueError:  
                    selecting = True  
                    cost = input("Invalid input, please input a decimal number: ")
            cost = cost[:cost.find('.') + 3]

            #Inputting the date aqquired requires it to follow a very specific format due to SQL's constraints on how a DATE type
            #Is formatted so these checks make sure that the correct form is followed
            dateAqquired = input("Please input the date the object was put into the permanent collection (XXXX-XX-XX [year - month - day]): ")
            selecting = True
            while selecting:
                if len(dateAqquired) == 10:
                    if dateAqquired.replace('-', '').isnumeric() and dateAqquired[4] == '-' and dateAqquired[7] == '-' and  int(dateAqquired[5:7]) <= 12 and int(dateAqquired[8:]) <=31:
                        selecting = False
                    else:
                        dateAqquired = input("Invalid date, please re enter the date the piece was aqquired: ")
                else:
                    dateAqquired = input("Invalid date, please re enter the date the piece was aqquired: ")
            #Creation of the command for inserting a new permanent collection value, using the values just inputted
            ternaryCommand = f"INSERT INTO PERMANENT_COLLECTION VALUES ('{ID_no}','{objStatus}','{cost}','{dateAqquired}');"

        #Same code as permanent collection but for the borrowed collections, it involes inputting the collectio ID as well which is checked for duplicates
        if Collection_type == 'Borrowed':
            
            selecting = True
            while selecting:
                #Input the collection ID
                collectionBorrowedFrom = input("Please input the collection the piece was borrowed from: ")
                if collectionBorrowedFrom not in getCurCollectionIDs(cur):
                    print("\nInvalid Input, Please input a collection ID that is already in the database\n")
                else:
                    selecting = False
            #Input the date it was borrowed
            dateBorrowed = input("Please input the date the object was borrowed on (XXXX-XX-XX [year - month - day]): ")
            selecting = True
            while selecting:
                if len(dateBorrowed) == 10:
                    if dateBorrowed.replace('-', '').isnumeric() and dateBorrowed[4] == '-' and dateBorrowed[7] == '-' and  int(dateBorrowed[5:7]) <= 12 and int(dateBorrowed[8:]) <=31:
                        selecting = False
                    else:
                        dateBorrowed = input("Invalid date, please re enter the date the piece was borrowed: ") 
                else:
                    dateBorrowed = input("Invalid date, please re enter the date the piece was borrowed: ")            

            #Input the date it was returned 
            dateReturned = input('Please input the date the object was returned on or \"None\" if it hasn\'t been (XXXX-XX-XX [year - month - day]): ')
            selecting = True
            if dateReturned == 'None':
                selecting = False
            while selecting:
                if dateReturned == 'None':
                    selecting = False
                    break

                if len(dateReturned) == 10:
                    if dateReturned.replace('-', '').isnumeric() and dateReturned[4] == '-' and dateReturned[7] == '-' and  int(dateReturned[5:7]) <= 12 and int(dateReturned[8:]) <=31:
                        selecting = False
                    else:
                        dateReturned = input("Invalid date, please re enter the date the piece was returned: ")
                else:
                    dateReturned = input("Invalid date, please re enter the date the piece was returned: ")
            
            #Considering the special case when date borrowed is null since in SQL it can't have quotations around it
            if dateReturned != 'None':
                ternaryCommand = f"INSERT INTO BORROWED VALUES ('{ID_no}','{collectionBorrowedFrom}','{dateBorrowed}','{dateReturned}');"
            else:
                ternaryCommand = f"INSERT INTO BORROWED VALUES ('{ID_no}','{collectionBorrowedFrom}','{dateBorrowed}', null);"
        
        #Inputting the type of art object that has been inserted to go through the creation process of insertting a tuple into
        #That specific table as well.
        print("What kind of art object are you inserting")
        selecting = True
        while selecting:
            i = input("(1) Painting \t (2) Statue \t (3) Sculpture \t (4) Other: ")
            if (i == '1'):

                #Inputs for a painting object
                objType = "Painting"
                paint_type = input("Please input the paint type: ")
                Drawn_on = input("Please input the medium the painting is drawn on: ")
                style = input("Please input the style of the painting: ")

                #Insert command creation for the object type
                secondary_Command = f"INSERT INTO PAINTING VALUES ('{ID_no}','{paint_type}','{Drawn_on}','{style}');"
                selecting = False
            elif (i == '2'):

                #Inputs for a statue object
                objType = "Statue"
                material = input("Please input the material the statue is made out of: ")
                
                selecting = True
                height = input("Please input the height of the statue: ")
                while selecting:
                    selecting = False
                    try:    
                        val = float(height) 
                    except ValueError:  
                        selecting = True  
                        height = input("Invalid input, please input a decimal number: ")

                selecting = True
                weight = input("Please input the weight of the statue: ")
                while selecting:
                    selecting = False
                    try:
                        val = float(weight)
                    except ValueError:
                        selecting = True
                        weight = input("Invalid input, please input a decimal number: ")

                style = input("Please input the style of the statue: ")

                #Insert command creation for the object type
                secondary_Command = f"INSERT INTO STATUE VALUES ('{ID_no}','{material}','{height}','{weight}','{style}');"
                selecting = False
            elif (i == '3'):

                #Inputs for a sculpture object
                objType = "Sculpture"
                material = input("Please input the material the sculpture is made out of: ")

                selecting = True
                height = input("Please input the height of the sculpture: ")
                while selecting:
                    selecting = False
                    try:    
                        val = float(height) 
                    except ValueError:  
                        selecting = True  
                        height = input("Invalid input, please input a decimal number: ")

                selecting = True
                weight = input("Please input the weight of the sculpture: ")
                while selecting:
                    selecting = False
                    try:
                        val = float(weight)
                    except ValueError:
                        selecting = True
                        weight = input("Invalid input, please input a decimal number: ")

                style = input("Please input the style of the sculpture: ")

                #Insert command creation for the object type
                secondary_Command = f"INSERT INTO SCULPTURE VALUES ('{ID_no}','{material}','{height}','{weight}','{style}');"
                selecting = False
            elif (i == '4'):

                #Inputs for other
                objType = "Other"
                other_type = input("Please input the type of this object: ")
                style = input("Please input this objects style: ")

                #Insert command creation for the object type
                secondary_Command = f"INSERT INTO OTHER VALUES ('{ID_no}','{other_type}','{style}');"
                selecting = False
            else:
                print("Invalid input")
                print()
            
        #Inputting the artist name and making sure it doesn't violate referential integrity nor be too long
        selecting = True
        while selecting:
            Artist_name = input("Please input the name of the artist who created the art object (input null if unknown): ")
            if Artist_name not in getCurArtistNames(cur) and Artist_name != 'null':
                print("\nInvalid Input, Please input an artist name that is already in the database\n")
            elif len(Artist_name) > 30:
                print("\nInvalid Input. Artist name must be less than 30 characters")
            
            else:
                selecting = False

        #Insert command for art object creation
        if (Artist_name != 'null'):
            art_obj_command = f"INSERT INTO ART_OBJECT VALUES ('{ID_no}','{Year_created}','{Title}','{Descr}','{Origin}','{Epoch}','{Collection_type}','{objType}','{Artist_name}');"
        else:
            art_obj_command = f"INSERT INTO ART_OBJECT VALUES ('{ID_no}','{Year_created}','{Title}','{Descr}','{Origin}','{Epoch}','{Collection_type}','{objType}',{Artist_name});"
        

        #Execution of the three insert commands
        cur.execute(art_obj_command)
        cur.execute(secondary_Command)
        cur.execute(ternaryCommand)

        #Displaying the updated table for art object 
        cur.execute("select * from art_object;")
        print(200*'~')
        print("Art Objects after insert")
        print()
        printData(cur.column_names, cur.fetchall(), 'Art Object')
        print(200*'~')

        print()

        #Prompting the user on if they want to see the changes to the specific object type table they added to as well
        showArtTypeChanges = input(f"{objType} has had an insert as well, would you like to see those changes? (Y or N): ")
        while showArtTypeChanges not in ['Y','N']:  showArtTypeChanges = input('Invalid input. (Y or N): ')
        if showArtTypeChanges == 'Y':
            cur.execute(f"select * from {objType};")
            print(200*'~')
            print(f"{objType} after insert")
            print()
            printData(cur.column_names, cur.fetchall())
            print(200*'~')

            print()

        #Prompting the user if they want to see the changes to the specific collection type table they added to as wel
        showCollectionTypeChanges = input(f"{Collection_type} collection has had an insert as well, would you like to see those changes? (Y or N): ")
        while showCollectionTypeChanges not in ['Y','N']:  showCollectionTypeChanges = input('Invalid input. (Y or N): ')
        if showCollectionTypeChanges == 'Y':

            c = 'PERMANENT_COLLECTION' if Collection_type == 'permanent' else 'BORROWED'

            cur.execute(f"select * from {c};")
            print(200*'~')
            print(f"{c} after insert")
            print()
            printData(cur.column_names, cur.fetchall())
            print(200*'~')

            print()

    if (actionType == "UPDATE"):
        #Check if their updating a specific art object or if its a subclass of one
        print()
        print("What type of art object are you updating")
        selecting = True
        while selecting:
            i = input("(1) Art Object \t (2) Painting \t (3) Statue \t (4) Sculpture \t (5) Other: ")

            print()
            print('-----------------------------------------------------------------------------------------------------------')
            print('| at any point when inputting new values leave the space blank to leave the value as what it currently is |')
            print('-----------------------------------------------------------------------------------------------------------')
            print()
            #Art object update
            if (i == '1'):
                tableName = 'art_object'

                
                cur.execute(f"select * from {tableName};")
                print(200*'~')
                print(f"{tableName} before any changes")
                print()
                printData(cur.column_names, cur.fetchall(), 'Art Object')
                print(200*'~')
                print()
                #Getting the ID of the object and checking that it alreadys exist in the database
                selecting = True
                while selecting:
                    ID_no = input("Please input the ID number of the art object: ")
                    if ID_no not in getCurArtIDs(cur):
                        print("\nInvalid Input, Please input an ID of an art object that is already in the database\n")
                    else:
                        selecting = False

                #Inputting a new year
                uYear = input("Please input the year the art object was created: ")
                while len(uYear) != 4 and uYear != '': uYear = input("Invalid Input. Year must be 4 digits. Please input a new year: ")
                if uYear != '':
                    uYear = 'Year_created=\'' + uYear + '\','


                #Input the title and check its length
                uTitle = input("Please input the title of the art object: ")
                while len(uTitle) > 40: uTitle= input("Invalid Input. title must be less than 40 characters. Please input a new title: ")
                if uTitle != '':
                    uTitle = 'Title=\'' + uTitle + '\','

                #Input the description and check its length
                uDescr = input("Please input the description of the art object: ")
                while len(uDescr) > 40: uDescr =input("Invalid Input. Description must be less than 40 characters. Please input a new description: ")
                if uDescr != '':
                    uDescr = 'Descr=\'' + uDescr + '\','
                
                #Input the origin and check its length
                uOrigin = input("Please input the origin of the art object: ")
                while len(uOrigin) > 15: uOrigin =input("Invalid Input. Origin must be less than 15 characters. Please input a new origin: ")
                if uOrigin != '':
                    uOrigin = 'Origin=\'' + uOrigin + '\','

                #Input the epoch and check its length
                uEpoch = input("Please input the epoch of the art object: ")
                while len(uEpoch) > 15: uEpoch =input("Invalid Input. Epoch must be less than 15 characters. Please input a new epoch: ")
                if uEpoch != '':
                    uEpoch = 'Epoch=\'' + uEpoch + '\','


                selecting = True
                while selecting:
                    uCollection_type = input("Please input the collection type that the object resides in (Borrowed or Permanent): ")
                    if uCollection_type not in ['Borrowed', 'Permanent', '']:
                        print("\nInvalid input, please input choice exactly as shown\n")
                    else:
                        selecting = False
                if uCollection_type !='':
                    uCollection_type = 'Collection_type=\'' + uCollection_type + '\','

                selecting = True
                while selecting:
                    uArtist_name = input("Please input the new artist name: ")
                    if uArtist_name not in getCurArtistNames(cur) and uArtist_name != 'null' and uArtist_name != '':
                        print("\nInvalid Input, Please input an artist name that is already in the database\n")
                    elif len(uArtist_name) > 30:
                        print("\nInvalid Input. Artist name must be less than 30 characters")
                    else:
                        selecting = False

                if uArtist_name !='':
                    uArtist_name = 'Artist_name=\'' + uArtist_name + '\','

                setCommand = "SET " + uYear + uTitle + uDescr + uOrigin + uEpoch + uCollection_type + uArtist_name
                if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1]
                selecting = False

            #Painting update
            elif (i == '2'):
                tableName = 'painting'

                cur.execute(f"select * from {tableName};")
                print(200*'~')
                print(f"{tableName} before any changes")
                print()
                printData(cur.column_names, cur.fetchall(), 'Art Object')
                print(200*'~')
                print()
                #Getting the ID of the object and checking that it alreadys exist in the database
                selecting = True
                while selecting:
                    ID_no = input("Please input the ID number of the painting: ")
                    if ID_no not in getCurPaintingIDs(cur):
                        print("\nInvalid Input, Please input an ID of a painting that is already in the database\n")
                    else:
                        selecting = False


                uPaint_type = input("Please input the new paint type: ")
                if uPaint_type != '':
                    uPaint_type = 'Paint_type=\'' + uPaint_type + '\','

                uDrawn_on = input("Please input the new medium the painting is drawn on: ")
                if uDrawn_on != '':
                    uDrawn_on = 'Drawn_on=\'' + uDrawn_on + '\','

                uStyle = input("Please input the new style of the painting: ")
                if uStyle != '':
                    uStyle = 'Style=\'' + uStyle + '\','       

                setCommand = "SET " + uPaint_type + uDrawn_on + uStyle
                if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1]  
                selecting = False   

            #Statue update
            elif (i == '3'):
                tableName = 'statue'


                cur.execute(f"select * from {tableName};")
                print(200*'~')
                print(f"{tableName} before any changes")
                print()
                printData(cur.column_names, cur.fetchall())
                print(200*'~')
                print()
                #Getting the ID of the object and checking that it alreadys exist in the database
                selecting = True
                while selecting:
                    ID_no = input("Please input the ID number of the statue: ")
                    if ID_no not in getCurStatueIDs(cur):
                        print("\nInvalid Input, Please input an ID of a statue that is already in the database\n")
                    else:
                        selecting = False



                uMaterial = input("Please input the new material the statue is made out of: ")
                if uMaterial != '':
                    uMaterial = 'material=\'' + uMaterial + '\','

                uHeight = input("Please input the new height of the statue: ")
                selecting = True
                if uHeight == '':
                    selecting = False
                while selecting:
                    if uHeight == '':
                        selecting = False
                        break
                    selecting = False
                    try:    
                        val = float(uHeight) 
                    except ValueError:  
                        selecting = True  
                        uHeight = input("Invalid input, please input a decimal number: ")   

                if uHeight != '':
                    uHeight = 'height_cm=\'' + uHeight + '\','

                uWeight = input("Please input the new weight of the statue: ")
                selecting = True
                if uWeight == '':
                    selecting = False
                while selecting:
                    if uWeight == '':
                        selecting = False
                        break
                    selecting = False
                    try:
                        val = float(uWeight)
                    except ValueError:
                        selecting = True
                        uWeight = input("Invalid input, please input a decimal number: ") 


                if uWeight != '':
                    uWeight = 'weight_kg=\'' + uWeight + '\','

                uStyle = input("Please input the new style of the statue: ")
                if uStyle != '':
                    uStyle = 'Style=\'' + uStyle + '\','  

                setCommand = "SET " + uMaterial + uHeight + uWeight + uStyle
                if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1]   
                selecting = False

            #Sculpture Update
            elif (i == '4'):
                tableName = 'sculpture'

                cur.execute(f"select * from {tableName};")
                print(200*'~')
                print(f"{tableName} before any changes")
                print()
                printData(cur.column_names, cur.fetchall())
                print(200*'~')
                print()

                #Getting the ID of the object and checking that it alreadys exist in the database
                selecting = True
                while selecting:
                    ID_no = input("Please input the ID number of the sculpture: ")
                    if ID_no not in getCurSculptureIDs(cur):
                        print("\nInvalid Input, Please input an ID of a sculpture that is already in the database\n")
                    else:
                        selecting = False


                uMaterial = input("Please input the new material the sculpture is made out of: ")
                if uMaterial != '':
                    uMaterial = 'material=\'' + uMaterial + '\','

                uHeight = input("Please input the new height of the sculpture: ")
                selecting = True
                if uHeight == '':
                    selecting = False
                while selecting:
                    if uHeight == '':
                        selecting = False
                        break
                    selecting = False
                    try:    
                        val = float(uHeight) 
                    except ValueError:  
                        selecting = True  
                        uHeight = input("Invalid input, please input a decimal number: ")   

                if uHeight != '':
                    uHeight = 'height_cm=\'' + uHeight + '\','

                uWeight = input("Please input the new weight of the sculpture: ")
                selecting = True
                if uWeight == '':
                    selecting = False
                while selecting:
                    if uWeight == '':
                        selecting = False
                        break
                    selecting = False
                    try:
                        val = float(uWeight)
                    except ValueError:
                        selecting = True
                        uWeight = input("Invalid input, please input a decimal number: ") 

                if uWeight != '':
                    uWeight = 'weight_kg=\'' + uWeight + '\','

                uStyle = input("Please input the new style of the sculpture: ")
                if uStyle != '':
                    uStyle = 'Style=\'' + uStyle + '\','  

                setCommand = "SET " + uMaterial + uHeight + uWeight + uStyle
                if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1] 
                selecting = False  


            elif (i == '5'):
                tableName = 'other'

                cur.execute(f"select * from {tableName};")
                print(200*'~')
                print(f"{tableName} before any changes")
                print()
                printData(cur.column_names, cur.fetchall())
                print(200*'~')
                print()

                #Getting the ID of the object and checking that it alreadys exist in the database
                selecting = True
                while selecting:
                    ID_no = input("Please input the ID number of the object: ")
                    if ID_no not in getCurOtherIDs(cur):
                        print("\nInvalid Input, Please input an ID of a object in the other table that is already in the database\n")
                    else:
                        selecting = False       


                uOther_type = input("Please input the type of this object: ")
                if uOther_type != '':
                    uOther_type = 'other_type=\'' + uOther_type + '\','  

                uStyle = input("Please input the new style of the object: ")
                if uStyle != '':
                    uStyle = 'Style=\'' + uStyle + '\','  

                setCommand = "SET " + uOther_type + uStyle
                if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1]  
                selecting = False
            else:
                print("Invalid input")
                print()

        if setCommand == 'SET ':
            print('No changes were made')
            return

        print()
        cur.execute(f"UPDATE {tableName} " + setCommand + f" WHERE ID_no = " + ID_no + ';')

        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} after changes")
        print()
        printData(cur.column_names, cur.fetchall())
        print(200*'~')

    if (actionType == "DELETE"):
        #Print table before deletion 
        tableName = 'art_object'
        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Art Object')
        print(200*'~')
        print()

        #Getting the ID of the object and checking that it alreadys exist in the database
        selecting = True
        while selecting:
            ID_no = input("Please input the ID number of the art object: ")
            if ID_no not in getCurArtIDs(cur):
                print("\nInvalid Input, Please input an ID of an art object that is already in the database\n")
            else:
                selecting = False

        print()
        print('Object deleted from art_object and its respective type sub table')
        print()

        cur.execute(f"DELETE FROM art_object WHERE ID_no = " + ID_no)

        #Print table after deletion
        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} after any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Art Object')
        print(200*'~')
        print()


def editArtists(cur, actionType = None):
    #Asking the user what kind of action they would like to do on the art object tables
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
            print()
            print("Invalid input")
            print()


    if (actionType == "INSERT"):
        #display the current state of the artist table before changes
        cur.execute("select * from artist;")
        print(200*'~')
        print("Artists before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Artist')
        print(200*'~')
        print()
        #Getting the name of the artist and checking that it doesn't already exist in the database
        selecting = True
        while selecting:
            name = input("Please input the name of the artist: ")
            if name in getCurArtistNames(cur):
                print("\nInvalid Input, Please input an artist name that is not already in the database\n")
            elif len(name) > 30:
                print("Invalid input. Please input a name 30 characters or shorter")
            else:
                selecting = False

        date_born = input('Please input the date the artist was born (XXXX-XX-XX [year - month - day]): ')
        selecting = True
        if date_born == 'None':
            selecting = False
        while selecting:
            if len(date_born) == 10:
                if date_born.replace('-', '').isnumeric() and date_born[4] == '-' and date_born[7] == '-' and int(date_born[5:7]) <= 12 and int(date_born[8:]) <=31:
                    selecting = False
                else:
                    date_born = input("Invalid date, please re enter the date when the artist was born (XXXX-XX-XX [year - month - day]): ")
            else:
                date_born = input("Invalid date, please re enter the date when the artist was born (XXXX-XX-XX [year - month - day]): ")


        date_died = input('Please input the date the artist died (XXXX-XX-XX [year - month - day]): ')
        selecting = True
        if date_died == 'None':
            selecting = False
        while selecting:
            if len(date_died) == 10:
                if date_died.replace('-', '').isnumeric() and date_died[4] == '-' and date_died[7] == '-' and  int(date_died[5:7]) <= 12 and int(date_died[8:]) <=31:
                    selecting = False
                else:
                    date_died = input("Invalid date, please re enter the date when the artist died (XXXX-XX-XX [year - month - day]): ")
            else:
                date_died = input("Invalid date, please re enter the date when the artist died (XXXX-XX-XX [year - month - day]): ")


        country_of_origin = input('Please input the country the artist originated from: ')
        epoch = input('Please input the epoch the artist was most present in: ')
        main_style = input('Please input the main style of the artist: ')
        descr = input('Please input a description of the artist: ')
        print()
        if date_born == 'None' and date_died != 'None':
            art_obj_command = f"INSERT INTO ARTIST VALUES ('{name}',null,'{date_died}','{country_of_origin}','{epoch}','{main_style}','{descr}');"
        elif date_born != 'None' and date_died == 'None':
            art_obj_command = f"INSERT INTO ARTIST VALUES ('{name}','{date_born}',null,'{country_of_origin}','{epoch}','{main_style}','{descr}');"
        elif date_born == 'None' and date_died == 'None':
            art_obj_command = f"INSERT INTO ARTIST VALUES ('{name}',null,null,'{country_of_origin}','{epoch}','{main_style}','{descr}');"
        else:
            art_obj_command = f"INSERT INTO ARTIST VALUES ('{name}','{date_born}','{date_died}','{country_of_origin}','{epoch}','{main_style}','{descr}');"
        cur.execute(art_obj_command)

        cur.execute("select * from artist;")
        print(200*'~')
        print("Artists after any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Artist')
        print(200*'~')
        print()

    if (actionType == "UPDATE"):
        tableName = 'Artist'

        #display the current state of the artist table before changes
        cur.execute("select * from artist;")
        print(200*'~')
        print("Artists before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Artist')
        print(200*'~')
        print()
        #Getting the ID of the object and checking that it doesn't already exist in the database
        selecting = True
        while selecting:
            name = input("Please input the name of the artist whom you'd like to update the information of: ")
            if name not in getCurArtistNames(cur):
                print("\nInvalid Input, Please input an artist name that is already in the database\n")
            elif len(name) > 30:
                print("Invalid input. Please input a name 30 characters or shorter")
            else:
                selecting = False

        print()
        print('-----------------------------------------------------------------------------------------------------------')
        print('| at any point when inputting new values leave the space blank to leave the value as what it currently is |')
        print('-----------------------------------------------------------------------------------------------------------')
        print()

        uDate_born = input('Please input the new date the artist was born (XXXX-XX-XX [year - month - day]): ')
        selecting = True
        if uDate_born == 'None' or uDate_born == '':
            selecting = False
        while selecting:
            if len(uDate_born) == 10:
                if uDate_born.replace('-', '').isnumeric() and uDate_born[4] == '-' and uDate_born[7] == '-' and  int(uDate_born[5:7]) <= 12 and int(uDate_born[8:]) <=31:
                    selecting = False
                else:
                    uDate_born = input("Invalid date, please re enter the date when the artist was born (XXXX-XX-XX [year - month - day]): ")
            else:
                uDate_born = input("Invalid date, please re enter the date when the artist was born (XXXX-XX-XX [year - month - day]): ")

        if uDate_born == 'None':
            uDate_born = 'date_born=null,'
        elif uDate_born != '':
            uDate_born = 'date_born=\'' + uDate_born + '\','  
        

        uDate_died = input('Please input the new date the artist died (XXXX-XX-XX [year - month - day]): ')
        selecting = True
        if uDate_died == 'None' or uDate_died == '':
            selecting = False
        while selecting:
            if len(uDate_died) == 10:
                if uDate_died.replace('-', '').isnumeric() and uDate_died[4] == '-' and uDate_died[7] == '-' and  int(uDate_died[5:7]) <= 12 and int(uDate_died[8:]) <=31:
                    selecting = False
                else:
                    uDate_died = input("Invalid date, please re enter the date when the artist died (XXXX-XX-XX [year - month - day]): ")
            else:
                uDate_died = input("Invalid date, please re enter the date when the artist died (XXXX-XX-XX [year - month - day]): ")

        if uDate_died == 'None':
            uDate_died = 'date_died=null,'
        elif uDate_died != '':
            uDate_died = 'date_died=\'' + uDate_died + '\','  



        uCountry_of_origin = input('Please input the new country the artist originated from: ')
        if uCountry_of_origin != '':
            uCountry_of_origin = 'country_of_origin=\'' + uCountry_of_origin + '\','  

        uEpoch = input('Please input the new epoch the artist was most present in: ')
        if uEpoch != '':
            uEpoch = 'epoch=\'' + uEpoch + '\','          

        uMain_style = input('Please input the new main style of the artist: ')
        if uMain_style != '':
            uMain_style = 'main_style=\'' + uMain_style + '\','          

        uDescr = input('Please input a new description of the artist: ')
        if uDescr != '':
            uDescr = 'descr=\'' + uDescr + '\','  

        print()
        setCommand = "SET " + uDate_born + uDate_died + uCountry_of_origin + uEpoch + uMain_style + uDescr
        if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1] 

        if setCommand == 'SET ':
            print('No changes were made')
            return

        cur.execute(f"UPDATE {tableName} " + setCommand + f" WHERE artist_name = \'" + name + '\';')

        cur.execute("select * from artist;")
        print(200*'~')
        print("Artists after any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Artist')
        print(200*'~')
        print()

    if (actionType == "DELETE"):
        #display the current state of the artist table before changes
        cur.execute("select * from artist;")
        print(200*'~')
        print("Artists before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Artist')
        print(200*'~')
        print()

        #Getting the name of the artist and checking that it doesn't already exist in the database
        selecting = True
        while selecting:
            name = input("Please input the name of the artist whom you'd like to delete the information of: ")
            if name not in getCurArtistNames(cur):
                print("\nInvalid Input, Please input an artist name that is already in the database\n")
            elif len(name) > 30:
                print("Invalid input. Please input a name 30 characters or shorter")
            else:
                selecting = False

        print()
        print('Artist deleted')
        print()

        cur.execute(f"DELETE FROM artist WHERE artist_name = \'" + name + '\'')

        cur.execute("select * from artist;")
        print(200*'~')
        print("Artists after any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Artist')
        print(200*'~')
        print()


def editPermCollection(cur, actionType = None):
    tableName = 'permanent_collection'

    #Asking the user what kind of action they would like to do on the art object tables
    print()
    print('Note that to insert into or delete from the permanent collection, the art object menu must be used')
    print()
    print('Please follow the instructions to update a value')

    #Check if their updating a specific art object or if its a subclass of one
    print()
    
    print()
    print('-----------------------------------------------------------------------------------------------------------')
    print('| at any point when inputting new values leave the space blank to leave the value as what it currently is |')
    print('-----------------------------------------------------------------------------------------------------------')
    print()


    
    cur.execute(f"select * from {tableName};")
    print(200*'~')
    print(f"{tableName} before any changes")
    print()
    printData(cur.column_names, cur.fetchall())
    print(200*'~')
    print()
    #Getting the ID of the object and checking that it alreadys exist in the permanent collection
    selecting = True
    while selecting:
        ID_no = input("Please input the ID number of the art object you wish to update: ")
        if ID_no not in getCurPermCollectIDs(cur):
            print("\nInvalid Input, Please input an ID of an art object that is already in the permanent collection\n")
        else:
            selecting = False

    #Inputting a new object status
    selecting = True
    while selecting:
        uObjStatus = input("Please input the new status of the object (Displayed, Stored, Loaned): ")
        if uObjStatus not in ('Displayed', 'Stored', 'Loaned'):
            if uObjStatus == '':
                selecting = False
            else:
                print("Invalid input, please input Displayed, Stored or Loaned")
        else:
            selecting = False

    if uObjStatus != '':
        uObjStatus = 'object_status=\'' + uObjStatus + '\','


    #Input the cost
    selecting = True
    uCost = input("Please input the new cost of the art object: ")
    if uCost != '':
        while selecting:
            selecting = False
            try:    
                val = float(uCost) 
            except ValueError:  
                selecting = True  
                uCost = input("Invalid input, please input a decimal number: ")
        uCost = uCost[:uCost.find('.') + 3]

    if uCost != '':
        uCost = 'cost=\'' + uCost + '\','

    uDate_acquired = input('Please input the new date the object was aqquired on (XXXX-XX-XX [year - month - day]): ')
    selecting = True
    if uDate_acquired == '':
        selecting = False
    while selecting:
        if len(uDate_acquired) == 10:
            if uDate_acquired.replace('-', '').isnumeric() and uDate_acquired[4] == '-' and uDate_acquired[7] == '-' and  int(uDate_acquired[5:7]) <= 12 and int(uDate_acquired[8:]) <=31:
                selecting = False
            else:
                uDate_acquired = input("Invalid date, please re enter the date when the artist was born (XXXX-XX-XX [year - month - day]): ")
        else:
            uDate_acquired = input("Invalid date, please re enter the date when the artist was born (XXXX-XX-XX [year - month - day]): ")

    if uDate_aqquired != '':
        uDate_aqquired = 'date_aqquired=\'' + uDate_aqquired + '\','  

    setCommand = "SET " + uObjStatus + uCost + uDate_acquired
    if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1]
    selecting = False

    if setCommand == 'SET ':
        print('No changes were made')
        return

    cur.execute(f"UPDATE {tableName} " + setCommand + f" WHERE ID_no = " + ID_no + ';')

    cur.execute(f"select * from {tableName};")
    print(200*'~')
    print(f"{tableName} after any changes")
    print()
    printData(cur.column_names, cur.fetchall())
    print(200*'~')
    print()


def editBorrowCollection(cur, actionType = None):
    tableName = 'borrowed'

    #Asking the user what kind of action they would like to do on the art object tables
    print()
    print('Note that to insert into or delete from the borrowed collection, the art object menu must be used')
    print()
    print('Please following the instructions to update a value')

    #Check if their updating a specific art object or if its a subclass of one
    print()
    
    print()
    print('-----------------------------------------------------------------------------------------------------------')
    print('| at any point when inputting new values leave the space blank to leave the value as what it currently is |')
    print('-----------------------------------------------------------------------------------------------------------')
    print()


    
    cur.execute(f"select * from {tableName};")
    print(200*'~')
    print(f"{tableName} before any changes")
    print()
    printData(cur.column_names, cur.fetchall())
    print(200*'~')
    print()
    #Getting the ID of the object and checking that it alreadys exist in the permanent collection
    selecting = True
    while selecting:
        ID_no = input("Please input the ID number of the art object you wish to update: ")
        if ID_no not in getCurBorrowCollectIDs(cur):
            print("\nInvalid Input, Please input an ID of an art object that is already in the borrowed collection\n")
        else:
            selecting = False

    #Inputting a new object status
    uCollection = input("Please input the new collectioin the object was borrowed from, it must already be in the data base: ")
    selecting = True
    while selecting:
        if uCollection == '':
            selecting = False
        elif uCollection not in getCurCollectionIDs(cur):
            uCollection = input("\nInvalid Input, Please input the name of a collection that is already in the database: ")
        else:
            selecting = False
    
    if uCollection != '':
        uCollection = 'collection=\'' + uCollection + '\','



    uDate_borrowed = input('Please input the new date the object was borrowed on (XXXX-XX-XX [year - month - day]): ')
    selecting = True
    if uDate_borrowed == '':
        selecting = False
    while selecting:
        if len(uDate_borrowed) == 10:
            if uDate_borrowed.replace('-', '').isnumeric() and uDate_borrowed[4] == '-' and uDate_borrowed[7] == '-' and  int(uDate_borrowed[5:7]) <= 12 and int(uDate_borrowed[8:]) <=31:
                selecting = False
            else:
                uDate_borrowed = input("Invalid date, please re enter the date when the object was borrowed (XXXX-XX-XX [year - month - day]): ")
        else:
            uDate_borrowed = input("Invalid date, please re enter the date when the object was borrowed (XXXX-XX-XX [year - month - day]): ")

    if uDate_borrowed != '':
        uDate_borrowed = 'date_borrowed=\'' + uDate_borrowed + '\','  


   #Input the date it was returned 
    uDate_Returned = input('Please input the new date the object was returned on or \"None\" if it hasn\'t been (XXXX-XX-XX [year - month - day]): ')
    selecting = True
    if uDate_Returned == 'None' or uDate_Returned == '':
        selecting = False
    while selecting:
        if len(uDate_Returned) == 10:
            if uDate_Returned.replace('-', '').isnumeric() and uDate_Returned[4] == '-' and uDate_Returned[7] == '-' and  int(uDate_Returned[5:7]) <= 12 and int(uDate_Returned[8:]) <=31:
                selecting = False
            else:
                uDate_Returned = input("Invalid date, please re enter the new date the piece was returned: ")
        else:
            uDate_Returned = input("Invalid date, please re enter the new date the piece was returned: ")

    if uDate_Returned == 'None':
        uDate_Returned = 'date_returned=null,'
    elif uDate_Returned != '':
        uDate_Returned = 'date_returned=\'' + uDate_Returned + '\',' 


    setCommand = "SET " + uCollection + uDate_borrowed + uDate_Returned
    if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1]

    if setCommand == 'SET ':
        print('No changes were made')
        return

    cur.execute(f"UPDATE {tableName} " + setCommand + f" WHERE ID_no = " + ID_no + ';')

    cur.execute(f"select * from {tableName};")
    print(200*'~')
    print(f"{tableName} after any changes")
    print()
    printData(cur.column_names, cur.fetchall())
    print(200*'~')
    print()


def editExhibitions(cur, actionType = None):
    #Asking the user what kind of action they would like to do on the art object tables
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
            print()
            print("Invalid input")
            print()


    if (actionType == "INSERT"):
        tableName = 'exhibition'

        #display the current state of the exhibition table before changes
        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} before any changes")
        print()
        printData(cur.column_names, cur.fetchall())
        print(200*'~')
        print()
        #Getting the ID of the exhibition and checking that it isn't already exists in the database
        selecting = True
        while selecting:
            EX_ID = input("Please input the ID of the exhibition you'd like to insert: ")
            if EX_ID  in getCurExIDs(cur):
                print("\nInvalid Input, Please input an exhibition ID that isn't already in the database\n")

            elif len(EX_ID) != 5:
                print("\nInvalid Input, Please input an exhibition ID that is exactly 5 characters long\n")
            else:
                selecting = False

        start_Date = input('Please input the date the exhibition starts on (XXXX-XX-XX [year - month - day]): ')
        selecting = True
        while selecting:
            if len(start_Date) == 10:
                if start_Date.replace('-', '').isnumeric() and start_Date[4] == '-' and start_Date[7] == '-'  and int(start_Date[5:7]) <= 12 and int(start_Date[8:]) <=31:
                    selecting = False
                else:
                    start_Date = input("Invalid date, please re enter the date when the exhibition starts (XXXX-XX-XX [year - month - day]): ") 
            else:
                start_Date = input("Invalid date, please re enter the date when the exhibition starts (XXXX-XX-XX [year - month - day]): ") 
        

        end_Date = input('Please input the date the exhibition ends on (XXXX-XX-XX [year - month - day]): ')
        selecting = True
        while selecting:
            if len(end_Date) == 10:
                if end_Date.replace('-', '').isnumeric() and end_Date[4] == '-' and end_Date[7] == '-' and int(end_Date[5:7]) <= 12 and int(end_Date[8:]) <=31:
                    selecting = False
                else:
                    end_Date = input("Invalid date, please re enter the date when the exhibition ends (XXXX-XX-XX [year - month - day]): ") 
            else:
                end_Date = input("Invalid date, please re enter the date when the exhibition ends (XXXX-XX-XX [year - month - day]): ") 



        name = input('Please input the  name of the exhibition: ')

        print()
        exhibition_command = f"INSERT INTO EXHIBITION VALUES ('{EX_ID}','{start_Date}','{end_Date}','{name}');"
        cur.execute(exhibition_command)


        IDs_to_insert = {}
        print("Please input the art object IDs that are present within this exhibition, it must have at least one.")
        print("When you're finished inputting IDs just input nothing and the program will proceed")

        cur.execute(f"select * from art_object;")
        print(200*'~')
        print(f"current list of art objects")
        print()
        printData(cur.column_names, cur.fetchall(), 'Art Object')
        print(200*'~')
        print()

        #Getting the ID of the object and checking that it alreadys exist in the database
        selecting = True
        while selecting:
            ID_no = input("Please input the ID number of the art object: ")
            if ID_no == '':
                selecting = False
            elif ID_no not in getCurArtIDs(cur):
                print("\nInvalid Input, Please input an ID of an art object that is already in the database\n")
            elif ID_no in IDs_to_insert.keys():
                print("Invalid input, please input an ID that isn't already in the exhibition, an art piece can't be shown twice")
            else:
                IDs_to_insert.update({ID_no : EX_ID})

        for id in IDs_to_insert.keys():
            cur.execute(f"INSERT INTO DISPLAYED_IN VALUES ('{EX_ID}','{id}');")

        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} after any changes")
        print()
        printData(cur.column_names, cur.fetchall())
        print(200*'~')
        print()

        #Prompting the user on if they want to see the changes to the displayed in table they added to as well
        showArtTypeChanges = input("Would you like to see the changes to displayed in as well? (Y or N): ")
        while showArtTypeChanges not in ['Y','N']:  showArtTypeChanges = input('Invalid input. (Y or N): ')
        if showArtTypeChanges == 'Y':
            cur.execute(f"select * from displayed_in;")
            print(200*'~')
            print(f"displayed_in after inserts")
            print()
            printData(cur.column_names, cur.fetchall())
            print(200*'~')

            print()

    if (actionType == "UPDATE"):
        tableName = 'exhibition'

        #display the current state of the exhibition table before changes
        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} before any changes")
        print()
        printData(cur.column_names, cur.fetchall())
        print(200*'~')
        print()
        #Getting the ID of the exhibition and checking that it already exists in the database
        selecting = True
        while selecting:
            EX_ID = input("Please input the ID of the exhibition you'd like to update the information of: ")
            if EX_ID not in getCurExIDs(cur):
                print("\nInvalid Input, Please input an exhibition ID that is already in the database\n")
            else:
                selecting = False

        print()
        print('-----------------------------------------------------------------------------------------------------------')
        print('| at any point when inputting new values leave the space blank to leave the value as what it currently is |')
        print('-----------------------------------------------------------------------------------------------------------')
        print()

        uStart_Date = input('Please input the new date the exhibition starts on (XXXX-XX-XX [year - month - day]): ')
        selecting = True
        if uStart_Date == '':
            selecting = False
        while selecting:
            if len(uStart_Date) == 10:
                if uStart_Date.replace('-', '').isnumeric() and uStart_Date[4] == '-' and uStart_Date[7] == '-'  and int(uStart_Date[5:7]) <= 12 and int(uStart_Date[8:]) <=31:
                    selecting = False
                else:
                    uStart_Date = input("Invalid date, please re enter the date when the exhibition starts (XXXX-XX-XX [year - month - day]): ")
            else:
                uStart_Date = input("Invalid date, please re enter the date when the exhibition starts (XXXX-XX-XX [year - month - day]): ")
        if uStart_Date != '':
            uStart_Date = 'start_date=\'' + uStart_Date + '\','  
        

        uEnd_Date = input('Please input the new date the exhibition ends on (XXXX-XX-XX [year - month - day]): ')
        selecting = True
        if uEnd_Date == '':
            selecting = False
        while selecting:
            if len(uEnd_Date) == 10:
                if uEnd_Date.replace('-', '').isnumeric() and uEnd_Date[4] == '-' and uEnd_Date[7] == '-'  and int(uEnd_Date[5:7]) <= 12 and int(uEnd_Date[8:]) <=31:
                    selecting = False
                else:
                    uEnd_Date = input("Invalid date, please re enter the date when the exhibition ends (XXXX-XX-XX [year - month - day]): ")
            else:
                uEnd_Date = input("Invalid date, please re enter the date when the exhibition ends (XXXX-XX-XX [year - month - day]): ")
        if uEnd_Date != '':
            uEnd_Date = 'end_date=\'' + uEnd_Date + '\','   



        uName = input('Please input the new name of the exhibition: ')
        if uName != '':
            uName = 'ex_name=\'' + uName + '\','  

        print()
        setCommand = "SET " + uStart_Date + uEnd_Date + uName
        if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1] 

        if setCommand == 'SET ':
            print('No changes were made')
            return  

        cur.execute(f"UPDATE {tableName} " + setCommand + f" WHERE EX_ID = \'" + EX_ID + '\';')

        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} after any changes")
        print()
        printData(cur.column_names, cur.fetchall())
        print(200*'~')
        print()

    if (actionType == "DELETE"):
        tableName = 'Exhibition'
        #display the current state of the exhibition table table before changes
        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} before any changes")
        print()
        printData(cur.column_names, cur.fetchall())
        print(200*'~')
        print()

        #Getting the ID of the exhibition and checking that it already exists in the database
        selecting = True
        while selecting:
            EX_ID = input("Please input the name of the exhibition that you would like to delete the information of: ")
            if EX_ID not in getCurExIDs(cur):
                print("\nInvalid Input, Please input an ID of an exhibition that is already in the database\n")
            else:
                selecting = False

        print()
        print('Exhibition deleted')
        print()

        cur.execute(f"DELETE FROM {tableName} WHERE EX_ID = \'" + EX_ID + '\';')

        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print(f"{tableName} after any changes")
        print()
        printData(cur.column_names, cur.fetchall())
        print(200*'~')
        print()


def editSepCollections(cur, actionType = None):
    #Asking the user what kind of action they would like to do on the art object tables
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
            print()
            print("Invalid input")
            print()


    if (actionType == "INSERT"):
        tableName = 'collection'
        print()
        #display the current state of the collection table before changes
        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print("Collection before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Collection')
        print(200*'~')
        print()
        #Getting the name of the collection and checking that it doesn't already exist in the database
        selecting = True
        while selecting:
            c_name = input("Please input the name of the collection: ")
            if c_name in getCurCollectionIDs(cur):
                print("\nInvalid Input, Please input an collection name that is not already in the database\n")
            elif len(c_name) > 30:
                print("Invalid input. Please input a name 30 characters or shorter")
            else:
                selecting = False

        c_type = input('Please input the type of the collection, must be 20 characters or less: ')
        while len(c_type) > 20: c_type = input("Invalid input, please keep your input under 20 characters: ")
        descr = input("Please input the description of the collection, must be less than 60 characters: ")
        while len(descr) > 60: descr = input("Invalid input, please keep your description under 60 characters: ")
        address = input("Please input the address of the collection, must be 45 characters or less: ")
        while len(address) > 45: address = input("Invalid input, please keep your address under 45 characters: ")
        phone = input("Please input the phone number for the collection (all digits no spaces, dashes or brackets): ")
        while not phone.isnumeric() or len(phone) > 15: phone = input("Invalid input, please only input digits and have your input be under 15 digits: ")
        cp_firstName = input("Please input the first name of the contact person for the collection, must be 15 characters or less: ")
        while len(cp_firstName) > 15: cp_firstName = input("Invalid input, must be less than 15 characters: ")
        cp_lastName = input("Please input the last name of the contact person for the collection, must be 15 characters or less: ")
        while len(cp_lastName) > 15: cp_lastName = input("Invalid input, must be less than 15 characters: ")

        print()
        art_obj_command = f"INSERT INTO COLLECTION VALUES ('{c_name}','{c_type}','{descr}','{address}','{phone}','{cp_firstName}','{cp_lastName}');"

        cur.execute(art_obj_command)

        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print("Collection after any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Collection')
        print(200*'~')
        print()

    if (actionType == "UPDATE"):
        tableName = 'collection'
        print()
        #display the current state of the collection table before changes
        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print("Collection before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Collection')
        print(200*'~')

        print()
        print('-----------------------------------------------------------------------------------------------------------')
        print('| at any point when inputting new values leave the space blank to leave the value as what it currently is |')
        print('-----------------------------------------------------------------------------------------------------------')
        print()

        #Getting the name of the collection and checking that it doesn't already exist in the database
        selecting = True
        while selecting:
            c_name = input("Please input the name of the collection: ")
            if c_name not in getCurCollectionIDs(cur):
                print("\nInvalid Input, Please input an collection name that is already in the database\n")
            else:
                selecting = False

        uC_type = input('Please input the new type of the collection, must be 20 characters or less: ')
        while len(uC_type) > 20 and uC_type != '': uC_type = input("Invalid input, please keep your input under 20 characters: ")
        if uC_type != '':
            uC_type = 'c_type=\'' + uC_type + '\',' 

        uDescr = input("Please input the new description of the collection, must be less than 60 characters: ")
        while len(uDescr) > 60 and uDescr != '': uDescr = input("Invalid input, please keep your description under 60 characters: ")
        if uDescr != '':
            uDescr = 'descr=\'' + uDescr + '\',' 
        
        uAddress = input("Please input the new address of the collection, must be 45 characters or less: ")
        while len(uAddress) > 45 and uAddress != '': uAddress = input("Invalid input, please keep your address under 45 characters: ")
        if uAddress != '':
            uAddress = 'address=\'' + uAddress + '\',' 

        uPhone = input("Please input the new phone number for the collection (all digits no spaces, dashes or brackets): ")
        while (not uPhone.isnumeric() or len(uPhone) > 15) and uPhone != '': uPhone = input("Invalid input, please only input digits and have your input be under 15 digits: ")
        if uPhone != '':
            uPhone = 'phone=\'' + uPhone + '\',' 

        uCp_firstName = input("Please input the new first name of the contact person for the collection, must be 15 characters or less: ")
        while len(uCp_firstName) > 15 and uCp_firstName != '': uCp_firstName = input("Invalid input, must be less than 15 characters: ")
        if uCp_firstName != '':
            uCp_firstName = 'cp_first_name=\'' + uCp_firstName + '\',' 
        
        uCp_lastName = input("Please input the new last name of the contact person for the collection, must be 15 characters or less: ")
        while len(uCp_lastName) > 15 and uCp_lastName != '': uCp_lastName = input("Invalid input, must be less than 15 characters: ")
        if uCp_lastName != '':
            uCp_lastName = 'cp_last_name=\'' + uCp_lastName + '\',' 

        
        print()
        setCommand = "SET " + uC_type + uDescr + uAddress + uPhone + uCp_firstName + uCp_lastName
        if setCommand[len(setCommand) - 1] == ',': setCommand = setCommand[:len(setCommand) - 1] 

        if setCommand == 'SET ':
            print('No changes were made')
            return

        cur.execute(f"UPDATE {tableName} " + setCommand + f" WHERE c_name = \'" + c_name + '\';')

        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print("Collection after any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Collection')
        print(200*'~')
        print()
        
    if (actionType == "DELETE"):
        tableName = 'collection'
        #display the current state of the collection table before changes
        cur.execute(f"select * from {tableName};")
        print(200*'~')
        print("Collection before any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Collection')
        print(200*'~')
        print()

        #Getting the name of the collection and checking that it doesn't already exist in the database
        selecting = True
        while selecting:
            c_name = input("Please input the name of the collection: ")
            if c_name not in getCurCollectionIDs(cur):
                print("\nInvalid Input, Please input an collection name that is already in the database\n")
            else:
                selecting = False

        print()
        print('Collection deleted')
        print()

        cur.execute(f"DELETE FROM COLLECTION WHERE c_name = \'" + c_name + '\'')

        cur.execute("select * from collection;")
        print(200*'~')
        print("Collection after any changes")
        print()
        printData(cur.column_names, cur.fetchall(), 'Collection')
        print(200*'~')
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
