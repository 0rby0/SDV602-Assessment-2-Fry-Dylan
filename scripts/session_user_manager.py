# Handles the connection between the user and different remote sessions
from pymongo import MongoClient
from db_config import DBConfig

class SessionUserManager:
	def __init__(self):
		self.client = MongoClient(DBConfig().MONGO_URI)
		self.client.admin.command("ping")

  
	def get_collection(self, collection):
		"""Gets the specified collection from the remote database."""
		return self.client[DBConfig().SELECTED_DB][collection]
	
 
	def find_link(self, username, session_name):
		"""Finds the account with the given name which us attached to the given session in the remote database."""
		pulled_link = self.get_collection(DBConfig().SESSION_USER_COLLECTION).find_one({"username": username, "session": session_name})
  
		has_link = False
		if pulled_link:
			has_link = True

		return has_link

	
	def find_link_by_username(self, username):
		"""Finds all links for the given username."""
		pulled_link = self.get_collection(DBConfig().SESSION_USER_COLLECTION).find({"username": username})

		parsed_link = None
		for link in pulled_link:
			parsed_link = {"username": link["username"], "session": link["session"]}

		return parsed_link


	def find_link_by_session(self, session_name):
		"""Finds all links for the given session name."""
		pulled_link = self.get_collection(DBConfig().SESSION_USER_COLLECTION).find({"session": session_name})
		
		parsed_link = None
		for link in pulled_link:
			parsed_link = {"username": link["username"], "session": link["session"]}

		return parsed_link


	def create_link(self, username, session):
		"""Create a new link between the given user and the given session"""
		userdata = {"username": username, "session": session}
		self.get_collection(DBConfig().SESSION_USER_COLLECTION).insert_one(userdata)
		return "User linked to session"


	def break_link(self, username, session_name):
		"""Deletes the link between the given user and the given session if applicable"""
		if not self.find_link(username, session_name):
			return False

		self.get_collection(DBConfig().SESSION_USER_COLLECTION).delete_one({"username": username, "session": session_name})
		return True