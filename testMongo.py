import pymongo
client = pymongo.MongoClient('mongodb://6c89938c-6b23-4f73-9c2b-7b3d390e2dec:DoAHSLsWsGgyim71Ke8G0D2Nb@40.83.74.54:27017/32580e61-969a-4b67-b31d-db0faa896b23')
db = client['']
cursor = db.temp.find()
for e in cursor:
    print e
