import mysql.connector
from GlobalFunctions import *
from DataEntryUserFunctions import *
from AdminUserFunctions import *

#Guest user search functions
def searchArtObjects(searchItem, cur):

    showArtists = input("Do you want to see the artist who created each piece as well? (Y  or N): ")
    showCollection = input("Do you want to see the collection each piece comes from (Y or N): ")
    showDetailedInfo = input("Would you like extra details such as the pieces origin or epoch (Y or N): ")

    options = ''
    
    #options will append the choices to the query afterwards, which will execute depending on inputs here
    if showArtists.upper() == 'Y':
        options += ', Artist_name'
    if showCollection.upper() == 'Y':
        options += ', Collection_Type'
    if showDetailedInfo.upper() == 'Y':
        options += ', Epoch, Origin'
    
    #query takes in all the options from if statements above
    print()
    query =f"SELECT Title{options} FROM art_object WHERE object_type LIKE '{searchItem}';"
    cur.execute(query)
    searchResult = cur.fetchall()
    printData(cur.column_names, searchResult)
    print()


def searchArtists(searchItem, cur):

    if searchItem == "Name":
        artistName = input("Please input the artists name you're interested in: ")
        print()
        query = f"SELECT Artist_name, Title FROM art_object WHERE Artist_Name like '%{artistName}%'"
        cur.execute(query)
        searchResult = cur.fetchall()
        if len(searchResult) == 0: #if searchResult is empty, then just return
            print("No artists found with this search.")
            print()
            return
        printData(cur.column_names, searchResult)
        print()

        showOrigin = input("Would you like to see the origin of the pieces this artist created? (Y or N): ") 
        if showOrigin.upper() == 'Y':
            query = f"SELECT Artist_name, Title, Origin FROM art_object WHERE Artist_Name like '%{artistName}%'"
            cur.execute(query)
            searchResult = cur.fetchall()
            printData(cur.column_names, searchResult)
            print()

    elif searchItem == "Epoch":
        artistEpoch = input("Please input the Epoch of the artist you're interested in: ")
        print()
        query = f"SELECT Artist_name, Epoch, Title FROM art_object WHERE Epoch like '%{artistEpoch}%'"
        cur.execute(query)
        searchResult = cur.fetchall()
        if len(searchResult) == 0: #if searchResult is empty, then just return
            print("No epochs found with this search.")
            print()
            return
        printData(cur.column_names, searchResult)
        print()


    elif searchItem == "All":
        cur.execute('SELECT Artist_Name FROM art_object WHERE Artist_Name IS NOT NULL')
        searchResult = cur.fetchall()
        printData(cur.column_names, searchResult)



def searchExhibitions(searchItem, cur):

    if searchItem == "ID":
        ExhibID = input("Please input the ID of the exhibit you're interested in: ")
        print()
        query = f"SELECT * FROM exhibition WHERE EX_ID like '%{ExhibID}%'"
        cur.execute(query)
        searchResult = cur.fetchall()
        if len(searchResult) == 0: #if searchResult is empty, then just return
            print("No exhibition ID matches with this search.")
            print()
            return
        printData(cur.column_names, searchResult)
        print()
        
    elif searchItem == "Name":
        ExhibName = input("Please input the name of the exhibit you're interested in: ")
        print()
        query = f"SELECT * FROM exhibition WHERE EX_name like '%{ExhibName}%'"
        cur.execute(query)
        searchResult = cur.fetchall()
        if len(searchResult) == 0: #if searchResult is empty, then just return
            print("No exhibition names matches with this search.")
            print()
            return
        printData(cur.column_names, searchResult)
        print()





#Guest Console
def guest_console(cur):
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
            print("Please input the kind of art pieces you're interested in viewing:")
            mLevelTwoChoice = input("(1) Painting \t (2) Sculpture \t (3) Statue \t (4) Other \t (0) Go Up a Level: ")
            print()
            print()

            if mLevelTwoChoice == '1':
                searchArtObjects("Painting", cur)
            elif mLevelTwoChoice == '2':
                searchArtObjects("Sculpture", cur)
            elif mLevelTwoChoice == '3':
                searchArtObjects("Statue", cur)
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
            print("Please input the part of the database you're interested in viewing:")
            mLevelTwoChoice = input("(1) Search Artist by Name \t (2) Search Artist by Epoch \t (3) See a list of all artists \t (0) Go Up a Level: ")
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
            print("Please input the part of the database you're interested in viewing:")
            mLevelTwoChoice = input("(1) Search Exhibitions by ID \t (2) Search Exhibitions by Name \t (0) Go Up a Level: ")
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
