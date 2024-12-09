## getting started with supabase with python

1. First of all you need to install supabase.
Ensure you are in a virtual environment.
Create a virtual environment using:
```sh
python3 -m venv myvenv
```

myvenv is the name of your virtual environment you can name it something else.

```sh
cd myvenv
```

activate by sourcing the activate file in bin directory.

```
source bin/activate
```

Install supabase once you are in the virtual environment
```sh
pip install supabase
```



## Initializing
You can initialize a new supabase client using the `create_client()` method.
The supabase client is the entry point to the rest of the supabase functionality.

### Parameters
Now supabase requires 2 mandatory parameters to the `create_client()` method.

1. supabase_url - REQUIRED
This is a unique supabase url which is given when you create a new project in your project dashboard.

2. supabase_key - REQUIRED
This is a unique supabase key which is also supplied when you create a new project in your project dashboard.

3. Options - OPTIONAL
This options paramether changes the Auth behaviours.
-	schema - Optional - string:
	- The postgres schema which your tables belong to. Must be on list of exposed schemas in supabase and it defaults to 'public'

- headers - Optional - dictionary:
	- Optional headers for initializing the client

- auto_refresh_token - Optional - bool
	- This indicates whether to automatically refresh the token when it expires. Defaults to `true`.

- persist_session - Optional - bool
	- whether to persist a logged in session to storage
	- this ensures at least for the duration of the session or amount of time, the client will connect
	with the same server
	- a session can be persisted so that the user is not required to authenticate each time they access a site.

- storage - Optional - SyncSupportedStorage
	- a storage provider. used to store the logged in session

- realtime - Optional - string
	- Options passed to the realtime-py instance.

- storage_client_timeout - Optional - number,float,timeout
	- timeout passed to the SyncStorageClient instance.

- flow_type Optional AuthFlowType
	- flow type to use for authentication

### creating a client
```py
import os
from supabase import create_client, Client
url: str  = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url,key)
```

## Fetching data
By default, supabase projects return a maximum of 1,000 rows. This setting can be changed in
[API settings].
It is recommended that you keep it low to limit the payload size of accidental or malicious requests.

You can use `range()` queries to paginate through your data.

`select()` can be combined with filters
`select()` can be combined with modifiers
`apikey` is a reserved word, dont use it as column name

### parameters
columns - Optional - string
- the columns to retrive defaults to `*`.

count - Optional - CountMethod
- The property to use to get the count of rows returned

To load environment variables use `python-dotenv`, this is because `dotenv` package is old and rarely
maintainde.
To install `python-dotenv`

```sh
pip install python-dotenv
```
From the `python-dotenv` package import `load_dotenv` to load `.env` files to your current file.



## EXAMPLES OF FETCHING DATA
Lets say you have a table called `members` and you want to fetch all the members from that table.
```py
response = supabase.table("members").select("*").execute()
```
- .table selects the table
- * means all
- .execute() executes the command and returns the response


