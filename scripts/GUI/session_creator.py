import FreeSimpleGUI as sg

class SessionCreator:
	def __init__(self, app):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app
		self.app = app

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
					case sg.WINDOW_CLOSED:
						break

					case _:
						pass

		self.window.close()