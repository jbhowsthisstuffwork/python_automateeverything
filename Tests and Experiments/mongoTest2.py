import pymongo
client = pymongo.MongoClient("mongodb+srv://jacksonboyer:<password>@cluster0.is41t.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test