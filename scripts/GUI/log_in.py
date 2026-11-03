import FreeSimpleGUI as sg
from GUI.des_selection import DESSelection

class LogIn:
	def __init__(self, app):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app and current screen
		self.app = app
		self.showing_login_screen = True

		# Show the window
		self.show()
  
  
	def create_window(self):
		title = [ [sg.Text("DES Analysis App")] ]

		input_layout = [
											[ sg.Text(text = "Login", key = "-HEADING-") ],
											[ sg.Text("Username"), sg.Input(key = "-USERNAME-") ],
											[ sg.Text("Password"), sg.Input(key = "-PASSWORD-") ],
											[ sg.Button(button_text = "Submit", key = "-SUBMIT-") ],
											[ sg.Button("Don't have an account? Sign Up", key = "-TOGGLE-") ]
										]

		layout = [
							[ sg.Column(title), sg.Column(input_layout) ]
						]

		return sg.Window("DES Analysis App", layout = layout)
  
  
	def show(self):
			while True:
				event, values = self.window.read()

				match event:
					case "-SUBMIT-":
						if self.app.user is None: return
      
						if self.showing_login_screen:
							# Attempt to log the user in with the given username and password				
							if self.app.user.log_in_user(username = values["-USERNAME-"], password = values["-PASSWORD-"]) == "Login Success":
     							# If they have successfully logged in, open the session manager
								DESSelection().show(self.app)
								# Close this window
								break

						else:
							if self.app.user.register_user(username = values["-USERNAME-"], password = values["-PASSWORD-"]) == "User created successfully":
								# If it is successfull, open the DES selection window
								self.showing_login_screen = not self.showing_login_screen
								self.update_window()
					
					case "-TOGGLE-":
						# Switch between displaying the login and sign up screen
						self.showing_login_screen = not self.showing_login_screen
						self.update_window()
     
					case sg.WINDOW_CLOSED:
						break

					case _:
						# If there is no input then do nothing
						pass

			self.window.close()


	def update_window(self):
		# Update the window only if it has just changed
		if self.showing_login_screen:
			self.window["-HEADING-"].update(value = "Login")
			self.window["-TOGGLE-"].update(text = "Don't have an account? Sign Up")
		else:
			self.window["-HEADING-"].update(value = "Sign Up")
			self.window["-TOGGLE-"].update(text = "Already have an account? Log In")