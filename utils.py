import re

def parse_markdown(markdown):

	result = {
		"title" : "None",
		"date" : "unspecified",
		"type" : "unspecified",
		"tags" : [],
		"author" : "unspecified",
		"subject" : "unspecified",
		"readme" : "unspecified",
		"questions" : []
	}

	lines = markdown.split("\n")

	question_index = 0

	for line in lines:

		# check for metadata, which is formatted as a markdown comment
		pattern = re.compile(r"\[([a-z]+)\]: <> \((.+)\)")

		if (pattern.search(line)):

			if pattern.search(line).group(1).lower() == "date":

				result["date"] = pattern.search(line).group(2)

			elif pattern.search(line).group(1).lower() == "tags":

				result["tags"] = pattern.search(line).group(2).split(", ")

			elif pattern.search(line).group(1).lower() == "author":

				result["author"] = pattern.search(line).group(2)

			elif pattern.search(line).group(1).lower() == "type":

				result["type"] = pattern.search(line).group(2)

			elif pattern.search(line).group(1).lower() == "readme":

				result["readme"] = pattern.search(line).group(2)

			elif pattern.search(line).group(1).lower() == "subject":

				result["subject"] = pattern.search(line).group(2)

		# check for title
		if line[0:2] == "# ":

			result["title"] = line.strip("# ")

		# check for question
		elif line[0:3] == "## ":

			new_question = {
				"question_index" : question_index
			}

			new_question["text"] = line.strip("## ")

			result["questions"].append(new_question)

			question_index += 1

		# check for an answer
		elif line[0:5] == "#### ":

			result["questions"][question_index - 1]["answer"] = line.strip("#### ")

		# check for a multiple choice answer
		elif line[0:2] == "- ":

			try:

				result["questions"][question_index - 1]["choices"].append(line.strip("- "))

			except KeyError:

				result["questions"][question_index - 1]["choices"] = [line.strip("- ")]

		elif line != "":

			result["description"] = line

	return result
