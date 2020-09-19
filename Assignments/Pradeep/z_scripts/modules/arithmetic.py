def add(x,y):
	print("From another script: ", __name__)
	return x+y
	
def sub(x,y):
	print("From another script: ", __name__)
	return x-y
	


if __name__ == "__main__" : # check if script is being imported or executed directly
	print("My Script: ", __name__)
	print("Answer: ", add(5, 10))