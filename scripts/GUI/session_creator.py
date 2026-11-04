import FreeSimpleGUI as sg

class SessionCreator:
	def __init__(self, app, des_selection_window):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app and DES selection window
		self.app = app
		self.des_selection_window = des_selection_window

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
						self.app.sm.create_session(session_name = values["-SESSIONNAME-"], public = values["-PUBLICTOGGLE-"], redirect = False)
						self.des_selection_window.window.un_hide()
						self.des_selection_window.show()
						self.window.close()

					case "-CANCEL-":
						self.des_selection_window.window.un_hide()
						self.window.close()

					case sg.WINDOW_CLOSED:
						self.des_selection_window.window.un_hide()
						break

					case _:
						pass

		self.close_window()


	def close_window(self):
		if self.des_selection_window:
			self.des_selection_window.close_window()

		self.window.close()
		