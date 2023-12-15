from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31821
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        

# Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary            
            if insert !=0:
                return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
# Method to implement the R in CRUD.    
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria, {"_id":False}) #using find() 
        else:
            data = self.database.animals.find({}, {"_id":False})
        return data

# Method to implement the U in CRUD.
    def update(self, first, change):
        if first is not None:
            if self.database.animals.count_documents(first, limit = 1) != 0:
                update_result = self.database.animals.update_many(first, {"$set": change})
                result = update_result.raw_result
            else:
                result = "Document not found"
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty")

# Method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "Document not found"
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")