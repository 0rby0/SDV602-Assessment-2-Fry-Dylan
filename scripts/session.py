# A session being hosted with its own chat, data and users.
from file_manager import FileManager
from database_connect import DatabaseConnection
from chat import Chat

class Session:
	def __init__(self, name, user = None, public = True):
		self.session_name = name
		self.creator = user
		self.public = public
  
		self._files = FileManager()
		
		self.db = None
		self._chat = None
  
		if user is not None:
			self._chat = Chat()
			self.db = DatabaseConnection()
			self.db.pull_data(self)
			self.db.push_data(self)
   
   
	def new_dataset(self, name):
		"""Creates a new dataset entry and pushes it to the database - Currently doesn't save without adding data to the dataset."""
		self._files.create_dataset(name)

		if self.db:
			self.db.push_data(self)

		return f"Dataset '{name}' successfully created"
   
   
	def add_datasource(self, file, dataset):
		"""Attempts to read a given CSV file and add its data to the internal and remote storage, marked as the given dataset."""
		if self._files.load_data_source(file, dataset) != "File loaded successfully":
			return "Failed to load file"
  
		if self.db:
			self.db.push_data(self)

		return f"Datasource '{file}' successfully added to '{dataset}'"
  
  
	def remove_dataset(self, name):
		"""Removes a dataset and all of its attached data from the internal and remote storage."""
		self._files.remove_dataset(name)
  
		if self.db:
			self.db.push_data(self)

		return f"Dataset '{name}' successfully removed"


	def remove_datasource(self, file, dataset):
		"""Attempt to remove the data of the requested file (e.g. document.csv), which is linked to the given dataset, from the internal and external databases."""
		self._files.remove_data_source(file, dataset)
  
		if self.db:
			self.db.push_data(self)

		return f"Datasource '{file}' successfully removed from '{dataset}'"


	def rename_dataset(self, old_name, new_name):
		"""Attempts to change all instances of the old name to the new name."""
		self._files.rename_dataset(old_name, new_name)
  
		if self.db:
			self.db.push_data(self)
  
		return f"Dataset '{old_name}' successfully renamed to '{new_name}'"


	def compile_dataset(self, dataset):
		"""Updates the internal database to use the remote data and then gathers all of the data, from the internal database, whichs is linked to the given dataset and combines it into one array."""
		if self.db:
			self.db.pull_data(self)
   
		return self._files.compile_dataset(dataset)


	def send_message(self, sender, contents):
		"""Sends a message to the remote database."""
		if self._chat and self.db:
			self._chat.send_message(sender, contents)
			self.db.push_data(self)
			return "Message sent"

		return "Messages can only be sent in remote sessions"


	def get_messages(self):
		"""Retrieves all of the messages for the current session and formats them."""
		if self._chat and self.db:
			self.db.pull_data(self)
			return self._chat.get_messages()

		return "Messages can only be accessed in remote sessions"