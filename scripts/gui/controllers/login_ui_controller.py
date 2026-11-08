import FreeSimpleGUI as sg

from gui.layouts.login_ui_layout import LoginUILayout
from gui.controllers.des_browser_ui_controller import parse as parse_browser


def parse(session_manager):
	layout = LoginUILayout()
   
	window = sg.Window(title = "DES Analysis App", layout = layout.layout)
	showing_login_screen = True

	while True:
		event, values = window.read()

		match event:
			case "-SUBMIT-":
				if showing_login_screen:
					# Attempt to log the user in with the given username and password				
					if session_manager.user.log_in_user(username = values["-USERNAME-"], password = values["-PASSWORD-"]) == "Login Success":
						parse_browser(session_manager = session_manager, login_window = window)

				else:
					if session_manager.user.register_user(username = values["-USERNAME-"], password = values["-PASSWORD-"]) == "User created successfully":
						# If it is successfull, return to the login screen
						showing_login_screen = not showing_login_screen
						update_window(window = window, showing_login = showing_login_screen)
			
			case "-TOGGLE-":
				# Switch between displaying the login and sign up screen
				showing_login_screen = not showing_login_screen
				update_window(window = window, showing_login = showing_login_screen)

			case sg.WINDOW_CLOSED:
				break

	window.close()
	layout.terminate()


def update_window(window, showing_login):
	# Update the window only if it has just changed
	if showing_login:
		window["-HEADING-"].update(value = "Login")
		window["-TOGGLE-"].update(text = "Don't have an account? Sign Up")
	else:
		window["-HEADING-"].update(value = "Sign Up")
		window["-TOGGLE-"].update(text = "Already have an account? Log In")
