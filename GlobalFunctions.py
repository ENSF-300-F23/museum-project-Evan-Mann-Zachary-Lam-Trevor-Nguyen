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

#Print function to print any set of data granted the header and data are provided
def printData(header, data):
    header_size=len(header)
    for i in range(header_size):
        print("{:<15s}".format(data[i]),end='')
    print()
    print(15*header_size*'-')
    for row in data:
        for val in row:
            print("{:<15s}".format(str(val)),end='')
        print()