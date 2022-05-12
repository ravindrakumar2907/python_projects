import pymongo


class MongoDBConnection:
    @staticmethod
    def get_myconnection(database_name):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient[database_name]
        return mydb
    
    @staticmethod
    def get_mycollection(database_name, collection_name):
        mydb = MongoDBConnection.get_myconnection(database_name)
        my_collection = mydb[collection_name]
        return my_collection
    




#data = MongoDBConnection()
#con = data.get_mycollection("test", "adityaBirla")
#print(con)

