import pymongo

myclient = pymongo.MongoClient("mongodb+srv://jacksonboyer:rFBzJ2rXcPK7@cluster0.is41t.mongodb.net/<dbname>?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

