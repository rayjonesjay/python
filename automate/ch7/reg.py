#!/usr/bin/env python3
import re 
number = input()

pattern = r"(\d{3})[\-.,](\d{3}[\-,.]\d{4})"
renumber = re.compile(pattern)

mo = renumber.search(number)

if mo:
    #reverse the output matched.
    print(mo.groups()[::-1])
    print(mo.group())
    print(mo.group(1))
    print(mo.group(2))
else:
    print("none")