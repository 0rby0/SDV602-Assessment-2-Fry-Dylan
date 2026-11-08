# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from headless import HeadlessTest

from session_manager import SessionManager
from session import Session

from gui.controllers.login_ui_controller import parse as parse_login
from gui.controllers.des_ui_controller import parse as parse_des

import argparse

import ctypes
import os

class App():
	def __init__(self, REMOTE : bool, verbosity : int):
		if os.name == "nt":
			try:
				ctypes.windll.shcore.SetProcessDpiAwareness(2)
			except Exception:
				try:
					ctypes.windll.user32.SetProcessDPIAware()
				except Exception:
					pass

		self.remote = REMOTE

		self.sm = SessionManager()
		
		if not REMOTE:
			self.sm.sessions.append(Session("Local Session", self.sm.user))
	
		if verbosity >= 0:
			HeadlessTest(self, verbosity = verbosity)
		else:
			if REMOTE:
				parse_login(self.sm)
			else:
				parse_des(self.sm, "Local Session")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("-r", "--Remote", help="execute the app in remote mode, leave off for local mode", action="store_true")
	parser.add_argument("-t", "--Test", choices=[0, 1, 2, 3], default=-1, type=int, help="run the app in headless testing mode at the given verbosity level")
 
	args = parser.parse_args()
 
	App(REMOTE = args.Remote, verbosity = args.Test)