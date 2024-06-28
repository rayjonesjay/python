#!/usr/bin/env python3
import sys
import re 

phoneNumber = input("Enter number:> ")
if len(phoneNumber) < 12:
    print("number too short must be 12 characters long")
    sys.exit()


phonePattern = r"\d{3}[.,-]\d{3}[,.-]\d{4}"

regexPattern = re.compile(phonePattern)

matchObject = regexPattern.fullmatch(phoneNumber)
print("fullmatch",matchObject)

mo = regexPattern.match(phoneNumber)
if mo:
    print("fullmatch",mo.group())
else:
    pass

mo = regexPattern.search(phoneNumber)
print("search",mo.group())
