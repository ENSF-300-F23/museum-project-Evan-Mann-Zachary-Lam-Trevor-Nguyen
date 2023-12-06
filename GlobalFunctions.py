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

def getCurPaintingIDs(cur):
    cur.execute("select ID_no from painting;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurStatueIDs(cur):
    cur.execute("select ID_no from statue;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurSculptureIDs(cur):
    cur.execute("select ID_no from sculpture;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurOtherIDs(cur):
    cur.execute("select ID_no from other;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurPermCollectIDs(cur):
    cur.execute("select ID_no from permanent_collection;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurBorrowCollectIDs(cur):
    cur.execute("select ID_no from borrowed;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurExIDs(cur):
    cur.execute("select EX_ID from Exhibition;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

def getCurCollectionIDs(cur):
    cur.execute("select C_name from collection;")
    searchResult = cur.fetchall()
    return [str(x[0]) for x in searchResult]

#Print function to print any set of data granted the header and data are provided
def printData(header, data, type = 'basic'):
    if type == 'Art Object':

        header_size=len(header)
        print(f"{str(header[0]):<11s}{str(header[1]):<13s}{str(header[2]):<40s}{str(header[3]):<40s}{str(header[4]):<15s}{str(header[5]):<15s}{str(header[6]):<17s}{str(header[7]):<15s}{str(header[8]):<30s}",end='')
        print()
        print(200*'-')
        for row in data:
            print(f"{str(row[0]):<11s}{str(row[1]):<13s}{str(row[2]):<40s}{str(row[3]):<40s}{str(row[4]):<15s}{str(row[5]):<15s}{str(row[6]):<17s}{str(row[7]):<15s}{str(row[8]):<30s}",end='')
            print()
    

    elif type == 'Artist':
        header_size=len(header)
        print(f"{str(header[0]):<30s}{str(header[1]):<13s}{str(header[2]):<13s}{str(header[3]):<20s}{str(header[4]):<15s}{str(header[5]):<20s}{str(header[6]):<40s}",end='')
        print()
        print(200*'-')
        for row in data:
            print(f"{str(row[0]):<30s}{str(row[1]):<13s}{str(row[2]):<13s}{str(row[3]):<20s}{str(row[4]):<15s}{str(row[5]):<20s}{str(row[6]):<40s}",end='')
            print()

    else:
        header_size=len(header)
        for col_name in header:
            print(f"{col_name:<30s}",end='')
        print()
        print(200*'-')
        for row in data:
            for val in row:
                print("{:<30s}".format(str(val)),end='')
            print()