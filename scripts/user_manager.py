# Manage users in the database
from pymongo import MongoClient
from db_config import DBConfig

class UserManager:
	def __init__(self):
		self.client = MongoClient(DBConfig().MONGO_URI)
		self.client.admin.command("ping")
  
  
	def get_collection(self, collection):
		"""Gets the specified collection from the remote database."""
		return self.client[DBConfig().SELECTED_DB][collection]
	
 
	def find_user(self, username):
		"""Finds the account with the given name from the remote database."""
		return self.get_collection(DBConfig().USER_COLLECTION).find_one({"username": username})


	def create_user(self, username, hash):
		"""Add a new account to the database with a hashed password."""
		userdata = {"username": username, "hash": hash}
		self.get_collection(DBConfig().USER_COLLECTION).insert_one(userdata)
		return "User created successfully"


	def wipe_user(self, username):
		"""Wipes the user's data from the database"""
		if not self.find_user(username):
			return "User not in database"

		self.get_collection(DBConfig().USER_COLLECTION).delete_one({"username": username})
		return "User removed from database"