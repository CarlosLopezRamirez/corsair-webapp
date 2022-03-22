import pymongo

my_client = pymongo.MongoClient('mongodb+srv://admin:<admin>@corsairdb.qwaoy.mongodb.net/corsairdb?retryWrites=true&w=majority')
corsairdb = my_client.corsairdb

users = corsairdb.corsair_user

def getAllUsers():
    return list(users.find({ }))

def insertUser(doc):
    users.insert_one(doc)