# import json
#
# f = open("secret.json")
# raw = f.read()
# f.close()
#
# secret = json.loads(raw)

import os

mongo_uri = os.environ["MONGO_URI"]

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(mongo_uri)

db = client['tfmd']

docs = db.docs

def text_search(query_string):

	results = docs.find(
		{"$text": {"$search": query_string}},
		{"score": {"$meta": "textScore"}}
	)

	if results:

		result_array = []

		for result in results:

			#ObjectId has to be serialized to be JSON friendly
			result["_id"] = str(result["_id"])

			result_array.append(result)

		return (result_array[::-1])

	else:

		return None

def find_by_object_id(object_id):

	result = docs.find_one(
		{"_id": ObjectId(object_id)}
	)

	#ObjectId has to be serialized to be JSON friendly
	result["_id"] = str(result["_id"])

	if result:

		return result

	else:

		return None
