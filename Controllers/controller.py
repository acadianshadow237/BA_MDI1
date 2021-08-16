

import Models.my_tables_model as db1


def connectToDatabase(url):
    
    engine = db1.create_engine(url, echo=True)
    db1.init_model(engine)
    session = db1.DBSession()
    #setupDatabase(engine)
    return session 

def getSession(url):
    pass


def disconnectfromDatabase(my_session):
    my_session.close()
    pass

def setupDatabase(engine):
    """Setup the db, note that this will not upgrade already existing tables"""
    db1.metadata.create_all(engine)
    print ("db created")



def check_db_exists(current_self):
    if current_self.my_url is None:
        return None
    
    db_myBase = db1.gather_tables(current_self)

    if db_myBase == -1:
        return -1
    
    else: 
        return 1
   
    

def simpleUpdate(ID,nfieldName,newValue,tableName):

    if nfieldName.strip() == None or ID.strip() == None or tableName.strip() == None:
        return
    else:

        fieldID = ID.strip()
        fieldName = nfieldName.strip()
        fieldNewValue = newValue.strip()
        fieldTable = tableName.strip()

    my_sql= 'update "'+ fieldTable +'" set "' + fieldName +'" = '+ fieldNewValue + ' where "ID" = ' + '\'' +fieldID +'\''
    print(my_sql)


def writeLog(currentLog):
        pass
        
def get_county(session):
    db = Table('VCountyNames',metadata, autoload_with = engine)

    
        
##----------------------------------------------------------------------
#def addRecord(session, data):
#    """
#    Data should be a tuple of two dictionaries in the following format:
#    #"""
#    #("author":{"first_name":"John", "last_name":"Doe"},
#    # "book":{"title":"Some book", "isbn":"1234567890",
#    #         "publisher":"Packt"}
#    #)
  
#    session.add(book)
#    session.commit()

##----------------------------------------------------------------------

##----------------------------------------------------------------------
#def convertResults(results):
#    """
#    Convert results to OlvBook objects
#    """
#    print
#    books = []
#    for record in results:
#        author = "%s %s" % (record.person.first_name,
#                            record.person.last_name)
#        book = OlvBook(record.id, record.title, author,
#                       record.isbn, record.publisher,
#                       record.person.last_name,
#                       record.person.first_name
#                       )
#        books.append(book)
#    return books

##----------------------------------------------------------------------
#def deleteRecord(session, idNum):
#    """
#    Delete a record from the database
#    """
#    #record = session.query(db_mbmBook).filter_by(id=idNum).one()
#    #session.delete(record)
#    session.commit()

##----------------------------------------------------------------------
#def editRecord(session, idNum, row):
#    """
#    Edit a record
#    """
#    #record = session.query(db_mbmBook).filter_by(id=idNum).one()
#    #print
#    #record.title = row["title"]
#    #record.person.first_name = row["first_name"]
#    #record.person.last_name = row["last_name"]
#    #record.isbn = row["isbn"]
#    #record.publisher = row["publisher"]
#    session.add(record)
#    session.commit()

##----------------------------------------------------------------------
def getAllRecords(session):
    """
    Get all records and return them
    """
    result = session.query(db_mvm.VBase).order_by(db_mvm.VBase.Name,db_mvm.VBase.From).all()
    return result

##----------------------------------------------------------------------
#def searchRecords(session, filterChoice, keyword):
#    """
#    Searches the database based on the filter chosen and the keyword
#    given by the user
#    """
#    if filterChoice == "Author":
#        qry = session.query(db_mbmPerson)
#        result = qry.filter(db_mbmPerson.first_name.contains('%s' % keyword)).all()
#        records = []
#        for record in result:
#            for book in record.books:
#                records.append(book)
#        result = records
    
#    elif filterChoice == "Title":
#        qry = session.query(db_mbmBook)
#        result = qry.filter(db_mbmBook.title.contains('%s' % keyword)).all()
#    elif filterChoice == "ISBN":
#        qry = session.query(db_mbmBook)
#        result = qry.filter(db_mbmBook.isbn.contains('%s' % keyword)).all()
#    else:
#        qry = session.query(db_mbmBook)
#        result = qry.filter(db_mbmBook.publisher.contains('%s' % keyword)).all()
#    return result

#----------------------------------------------------------------------
