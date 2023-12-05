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
def printData(header, data, type = 'basic'):
    if type == 'Art Object':

        header_size=len(header)
        print(f"{str(header[0]):<11s}{str(header[1]):<6s}{str(header[2]):<25s}{str(header[3]):<25s}{str(header[4]):<20s}{str(header[5]):<15s}{str(header[6]):<15s}{str(header[7]):<15s}{str(header[8]):<20s}",end='')
        print()
        print(17*header_size*'-')
        for row in data:
            print(f"{str(row[0]):<11s}{str(row[1]):<6s}{str(row[2]):<25s}{str(row[3]):<25s}{str(row[4]):<20s}{str(row[5]):<15s}{str(row[6]):<15s}{str(row[7]):<15s}{str(row[8]):<20s}",end='')
            print()
    
    else:
        header_size=len(header)
        for col_name in header_size:
            print(f"{col_name:>15s}",end='')
        print()
        print(15*header_size*'-')
        for row in data:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()