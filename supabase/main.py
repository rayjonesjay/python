"""

this file contains code that I use to practice using supabase
read the readme.md file in order to understand how to use supabase with python
"""

import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url,key)

## update
response = (
	supabase.table("members")
	.update({"username":"nemesis"})
	.eq("id",1)
	.execute()
)
print(response)

"""

# insert data
response = (
	supabase.table("members")
	.insert({"id":2,"username":"ghost"})
	.execute()
)

# fetch data
response = supabase.table("members").select("*").execute()
if len(response.data) == 0:
	print("no data found")
else:
	print(response)

"""
