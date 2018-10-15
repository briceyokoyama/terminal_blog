import pymongo

class Database(object):

    #STATIC VARIABLES - URI & Database will always be the same in this project
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    @staticmethod #method belongs to the class as a whole - not an instance of a database
    def initialize():
        #Because URI is a static variable it must be accessed through the Database class
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)
    
    #returns cursor to first json object
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    #returns first json object
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)