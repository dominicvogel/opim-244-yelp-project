#this is the "app/yelp_load.py" file...

import os
from dotenv import load_dotenv

load_dotenv() #look in the ".env" file for env vars

API_KEY = os.getenv("API_KEY")
