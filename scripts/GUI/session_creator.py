import FreeSimpleGUI as sg

from session_manager import SessionManager

class SessionCreator:
	def __init__(self, des_selection_window):
		self.des_selection_window = des_selection_window

		# Create the window
		self.window = self.create_window()
		# Show the window
		self.show()


	def create_window(self):
		layout = [
							[ sg.Text("Create Session") ],
							[ sg.Text("Session Name"), sg.Input(key = "-SESSIONNAME-") ],
							[ sg.Button(button_text = "Cancel", key = "-CANCEL-"), sg.Checkbox(text = "Public", key = "-PUBLICTOGGLE-"), sg.Button(button_text = "Create", key = "-SUBMIT-") ]
						]

		return sg.Window("DES Analysis App", layout = layout)


	def show(self):
		while True:
			event, values = self.window.read()

			match event:
					case "-SUBMIT-":
						SessionManager().create_session(session_name = values["-SESSIONNAME-"], public = values["-PUBLICTOGGLE-"], redirect = False)
						self.window.close()
						self.des_selection_window.window.un_hide()
						self.des_selection_window.show()

					case "-CANCEL-":
						self.des_selection_window.window.un_hide()
						self.window.close()

					case sg.WINDOW_CLOSED:
						break

		self.close_window()


	def close_window(self):
		if self.des_selection_window:
			self.des_selection_window.close_window()

		self.window.close()
		