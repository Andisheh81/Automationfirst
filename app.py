import os
from dotenv import load_dotenv

# 1. Load the secrets from the hidden .env file
load_dotenv()

# 2. Grab the secret using the 'os' library
password = os.getenv("MY_SECRET_KEY")
user=os.getenv("last_name")

# 3. Print it out to prove Python found it
print("---------------------------------")
value = f"Success! your last name is :{user} The secret password is: {password}"
print(value)
print("---------------------------------")