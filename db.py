import json

f = open("secret.json")
raw = f.read()
f.close()

secret = json.loads(raw)

from pymongo import MongoClient

client = MongoClient(secret["mongo_uri"])

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

			result_array.append(result)

		return (result_array[::-1])

	else:

		return None

	
