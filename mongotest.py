import pymongo
import urllib.parse

username = urllib.parse.quote_plus('sutapabhattacharya')
password = urllib.parse.quote_plus('Bik@109836209')
client = pymongo.MongoClient("mongodb+srv://%s:%s@cluster0.b0bwa.mongodb.net/?retryWrites=true&w=majority" % (username, password))
db = client.test
print(db)

d = {
    "name" : "Sutapa" ,
    "email" : "sutapabhattacharya@xyz.com",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)