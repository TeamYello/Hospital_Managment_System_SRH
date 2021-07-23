from pymongo import MongoClient, GEO2D
db = MongoClient().test

#Creating  a spherical (earth-like) geospatial index
db.ambulances1.create_index([("location", GEO2D)])
# db.bar.create({point:"2dsphere"})

# result = db.ambulances1.insert_many([{"location": [77.58500266815773, 12.91755563735541]},{"location": [77.58521724488253, 12.916802709292165]},{"location": [77.57954966888413, 12.91662325031991]},{"location": [77.57740785084165, 12.919758726865274]},{"location": [77.5745626269674, 12.920934117797213]},{"location": [77.56550847857116, 12.921871894836329]},{"location": [77.56194013801044, 12.914054535609148]}]) 
# result.inserted_ids

#fetching all records
# for x in db.ambulances1.find():
#     print(x)

#finding documents near another point
#  for doc in db.ambulances1.find({"location": {"$near": [77, 12]}}).limit(3):
#     print(doc)

from bson.son import SON
query = {"location": SON([("$near", [77, 12]), ("$maxDistance", 1000)])}
# for doc in db.ambulances1.find(query).limit(3):
#      print(doc)



