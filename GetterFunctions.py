import mysql.connector

#Global Functions
def getCurArtistNames(cur):
    cur.execute("select artist_name from artist;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurArtIDs(cur):
    cur.execute("select ID_no from art_object;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurExIDs(cur):
    cur.execute("select EX_ID from Exhibition;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]