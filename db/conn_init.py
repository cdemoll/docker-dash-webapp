from pymongo import MongoClient
from secret_keys import *

#######################################SERVER#######################################
# Connect to remote MongoDB database
client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.yvr1zwc.mongodb.net/?retryWrites=true&w=majority",ssl=True, tlsAllowInvalidCertificates=True)
mydb = client[DB_NAME]