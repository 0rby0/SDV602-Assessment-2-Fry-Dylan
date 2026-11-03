import FreeSimpleGUI as sg

class ChatWindow:
	def __init__(self, app):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app
		self.app = app

		# Show the window
		self.show()
   
   
	def create_window(self):
		layout = [
							[ sg.Text("Session Name", size = (40, 1), justification = "center", key = "-SESSIONNAME-") ],
							[ sg.HorizontalSeparator() ],
							[ sg.Multiline(size = (47, 25), disabled = True, key = "-CHATLOG-") ],
							[ sg.Input(key = "-MESSAGEINPUT-"), sg.Button(">", key = "-SUBMIT-") ]
						]

		return sg.Window("DES Analysis App", layout = layout)
   
   
	def show(self):
		while True:
			event, values = self.window.read()

			match event:
					case sg.WINDOW_CLOSED:
						running = False
						break

					case _:
						break

		self.close_window()


	def close_window(self):
		self.window.close()