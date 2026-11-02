# Create, Delete, and load sessions
from database_connect import DatabaseConnection
from session_user_manager import SessionUserManager
from session import Session

class SessionManager:
	def __init__(self, user):
		self.sessions = []
		self.user = user
		self.link = SessionUserManager()
		self.db = DatabaseConnection()


	def get_remote_session_names(self):
		"""Retrieves and returns the names of all remote sessions being stored in the database."""
		session_list = []
		retrieved_sessions = self.db.get_all_sessions()

		if not retrieved_sessions:
			return "No sessions"
  
		for session in retrieved_sessions:
			if session["public"] == True:
				session_list.append(session["session"])

		return session_list


	def search_sessions(self, search_string):
		"""Return an array with the names of any remote sessions containing the search string"""
		matching_sessions = []
  
		for session in self.get_remote_session_names():
			if search_string in session:
				matching_sessions.append(session)

		if len(matching_sessions) == 0:
			return "No sessions found"

		return matching_sessions


	def join_session(self, session_name):
		"""Try to find the given session in the database and join if it exists"""
		for session in self.db.get_all_sessions():
			if session["session"] == session_name:
				self.link.create_link(username = self.user.username, session = session_name)
				self.sessions.append(Session(session_name, self.user.username))
				return f"Successfully joined session: '{session_name}'"
 
		return "Session not found"


	def create_session(self, session_name, public = True, redirect = False):
		"""Creates a new session in the session list if one does not exist"""
		
		# Check that a session doesn't already exist
		for session in self.db.get_all_sessions():
			if session["session"] == session_name:
				if redirect:
					return self.join_session(session_name)
				return "Session already exists"
 
 
		self.link.create_link(username = self.user.username, session = session_name)
		self.sessions.append(Session(session_name, self.user.username, public = public))
		return f"Successfully joined session: '{session_name}'"


	def remove_session(self, session_name, user):
		"""Attempt to remove the requested session from the database as the given user"""
		if not session_name:
			return "Invalid session name"

		if not user:
			return "Invalid user"

		for session in self.db.get_all_sessions():
			if session["session"] == session_name:
      
				if session["creator"] != user.username:
					return "User is not creator of session"

				if self.link.find_link_by_session(session_name):
					return "Cannot delete session, session in use"

				self.db.wipe_data(session)
				return f"Session '{session["session"]}' removed from database"
 
		return "Session not in database"
 

	def leave_session(self, session_name):
		"""Attempt to remove the session with the requested name from the session manager session list"""
		session_index = 0

		# Check if each session is the one being requested
		for session in self.sessions:
			if session_name == session.session_name:
				# Delete the current index from the main list if the names match
				self.sessions.remove(self.sessions[session_index])
				if self.link.break_link(username = self.user.username, session_name = session_name):
					return "Successfully left session"
				else:
					return "Failed to leave session"
			else:
				# Increase the index if the names don't match
				session_index += 1
   
		# Only show the error message if none of the names match
		return "Not in session"
		
		