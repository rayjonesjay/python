"""
Finding patterns of text with regular expressions
"""
import re

phoneNumberList = ["112-233-2233", "134-33-2323","200-111-2002"]

phoneNumberRegexObject = re.compile(r'\d{3}-\d{3}-\d{4}')
for phoneNumber in phoneNumberList:
	matchedObject = phoneNumberRegexObject.match(phoneNumber)
	if matchedObject != None:
		print("found:", matchedObject.group())
print("*"*10)

# search() method searches through a string for a particular pattern
# returns None if not found 

message = "Hello my number is 123-234-2343 see you later at 18:00"

matchedObject = phoneNumberRegexObject.search(message)
if matchedObject != None:
	print("found!",matchedObject.group())

# group() will return the whole match if found
