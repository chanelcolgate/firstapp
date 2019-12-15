import pymongo
client = pymongo.MongoClient('')
db = client['']
cursor = db.temp.find()
for e in cursor:
    print e
