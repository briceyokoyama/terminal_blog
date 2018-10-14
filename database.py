import pymongo

class Database(object):

    #STATIC VARIABLES
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    @staticmethod #Lets method use the static variables
    def initialize():
        #Because URI is a static variable it must be accessed through the Database class
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)
    
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)