import FreeSimpleGUI as sg
from GUI.sign_up import SignUp
from GUI.des_selection import DESSelection

class LogIn:
	 def show(self, app):
			title = [ [sg.Text("DES Analysis App")] ]

			input_layout = [
												[ sg.Text("Login") ],
												[ sg.Text("Username"), sg.Input(key = "-USERNAME-") ],
												[ sg.Text("Password"), sg.Input(key = "-PASSWORD-") ],
												[ sg.Button(button_text = "Submit", key = "-SUBMIT-") ],
												[ sg.Button("Don't have an account? Sign Up", key = "-SIGNUP-") ]
											]

			layout = [
								[ sg.Column(title), sg.Column(input_layout) ]
							]

			window = sg.Window("DES Analysis App", layout = layout)

			while True:
				event, values = window.read()

				match event:
					case "-SUBMIT-":
						# Attempt to log the user in with the given username and password
						if app.user is None: return
						if app.user.log_in_user(username = values["-USERNAME-"], password = values["-PASSWORD-"]) == "Login Success":
							# If they have successfully logged in, open the session manager
							DESSelection().show()
						# Close this window
						break
					
					case "-SIGNUP-":
						# Open the signup window
						SignUp().show()
						# Close this window
						break
     
					case sg.WINDOW_CLOSED:
						break

					case _:
						# If there is no input then do nothing
						pass

			window.close()