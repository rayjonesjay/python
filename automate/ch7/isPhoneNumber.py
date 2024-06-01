def isPhoneNumber(text):

	#if the length of the text is not 12 
	if len(text) != 12:
		return False 

	#if the first 3 characters of text are not decimal
	for i in range(0,3):
		if not text[i].isdecimal():
			return False 

	#if the fourth element is not a hiphen
	if text[3] != '-':
		return False 

	#if the fifth element through the seventh excluded are not decimal
	for i in range(4,7):
		if not text[i].isdecimal():
			return False 

	if text[7] != '-':
		return False 


	for i in range(8,12):
		if not text[i].isdecimal():
			return False

	return True 

phoneNumber="512-343-4344"
print(isPhoneNumber(phoneNumber))
phoneNumber="512-343-444" #not a valid phone number
print(isPhoneNumber(phoneNumber))
message = 'Call me at 415-1555-101 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
	currentTwelveItems = message[i:i+12]
	if isPhoneNumber(currentTwelveItems):
		print("Found Phone Number",currentTwelveItems)
"""
First three digits - 512 is the area code
"""