# Contains configuration settings for the database connection
import os

class DBConfig:
	instance = None
   
	def __new__(cls):
		if cls.instance is None:
			cls.instance = super().__new__(cls)
   
			cls.MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

			cls.DB_NAME = "des_app"
			cls.TEST_NAME = "debug-des_app"

			cls.SELECTED_DB = cls.DB_NAME

			cls.SESSION_COLLECTION = "sessions"
			cls.USER_COLLECTION = "users"
			cls.SESSION_USER_COLLECTION = "session_user"
   
		return cls.instance
 
	def use_db(self, db = "db"):
		match db:
			case "db": self.SELECTED_DB = self.DB_NAME
			case "test": self.SELECTED_DB = self.TEST_NAME