# Functions go here
def int_check(question):
	valid = False
	while not valid:
		try:
			response = int(input(question))
			if response >= 80:
				print("You are very old")
			elif response >=20 and response <=79:
				print("You are a grown up")
			elif response >= 12 and response <=19:
				print("You are a teenager")
			else:
				print("You are too young to be on a computer by yourself")

			break
		except ValueError:
			print("Not a valid age")
	return response


# Main routine goes here
age = int_check("What is your age? ")