# The user who is logged in to the application.
import bcrypt
from user_manager import UserManager

class User:
	def __init__(self):
		self.username = None


	def get_hash(self, password):
		"""Hashes a given string."""
		bytes = password.encode('utf-8')

		salt = bcrypt.gensalt()
		hash = bcrypt.hashpw(bytes, salt)
  
		return hash


	def register_user(self, username, password):
		"""Creates a new user in the remote database and sets the user object to them."""
		existing_user_check = UserManager().find_user(username)
  
		if existing_user_check:
			return "User already exists"

		self.username = username
		return UserManager().create_user(username, self.get_hash(password))


	def log_in_user(self, username, password):
		"""Finds the given username in the database, checks if the password hashes match and then sets the user object to it."""
		found_user = UserManager().find_user(username)

		if not found_user:
			return "Login Failed"

		if bcrypt.checkpw(password.encode('utf-8'), found_user["hash"]):
			self.username = found_user["username"]
			return "Login Success"
		else:
			return "Login Failed"


	def log_out(self):
		"""Unsets the current user if possible"""
		self.username = None
		return "Logged out"
  
  
	def delete_user(self):
		"""Removes the user from the database and signs them out"""
		if UserManager().wipe_user(self.username) == "User removed from database":
			self.username = None
			return "User deleted successfully"
		else:
			return "Failed to delete user"