import mysql.connector
from GetterFunctions import *
from DataEntryUserFunctions import *
from AdminUserFunctions import *


#Guest user search functions
def searchArtObjects(searchItem, cur):
    instr = ""
    join = ""

    showArtists = input("Do you want to see the artist who created each piece as well? (Y  or N): ")
    showCollection = input("Do you want to see the collection each piece comes from (Y or N): ")
    showDetailedInfo = input("Would you like extra details such as the pieces origin or epoch (Y or N): ")

def searchArtists(searchItem, cur):
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

def searchExhibitions(searchItem, cur):
    instr = ""
    join = ""

    if searchItem == "ID":
        artistName = input("Please input the ID of the exhibit you're interested in: ")
        
    elif searchItem == "Name":
        artistEpoch = input("Please input the name of the exhibit you're interested in: ")





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
