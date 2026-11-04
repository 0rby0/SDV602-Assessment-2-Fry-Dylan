# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from session import Session
from session_manager import SessionManager
from headless import HeadlessTest
from GUI.log_in import LogIn
from GUI.des_window import DESWindow
import argparse

class App():
	def __init__(self, REMOTE : bool, verbosity : int):
		self.remote = REMOTE
		self.sm = SessionManager()
		
		if not REMOTE:
			self.sm.sessions.append(Session("Local Session", self.sm.user))
	
		if verbosity >= 0:
			HeadlessTest(self, verbosity = verbosity)
		else:
			if REMOTE:
				LogIn(self)
			else:
				DESWindow(self, "Local Session")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("-r", "--Remote", help="execute the app in remote mode, leave off for local mode", action="store_true")
	parser.add_argument("-t", "--Test", choices=[0, 1, 2, 3], default=-1, type=int, help="run the app in headless testing mode at the given verbosity level")
 
	args = parser.parse_args()
 
	App(REMOTE = args.Remote, verbosity = args.Test)