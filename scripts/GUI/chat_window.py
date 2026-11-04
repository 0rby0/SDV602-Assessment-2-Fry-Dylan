import FreeSimpleGUI as sg

class ChatWindow:
	def __init__(self, app, session_id):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app
		self.app = app
		self.session_id = session_id

		# Show the window
		self.show()
   
   
	def create_window(self):
		layout = [
							[ sg.Text(self.app.sm.sessions[self.session_id].session_name, size = (40, 1), justification = "center") ],
							[ sg.HorizontalSeparator() ],
							[ sg.Multiline(size = (47, 25), disabled = True, key = "-CHATLOG-") ],
							[ sg.Input(key = "-MESSAGEINPUT-"), sg.Button(">", key = "-SUBMIT-") ]
						]

		return sg.Window("DES Analysis App", layout = layout)
   
   
	def show(self):
		while True:
			event, values = self.window.read(10)

			self.window["-CHATLOG-"].update(self.app.sm.sessions[self.session_id].get_messages())

			match event:
				case "-SUBMIT-":
					self.app.sm.sessions[self.session_id].send_message(self.app.user, values["-MESSAGEINPUT-"])

				case _:
					pass


	def close_window(self):
		self.window.close()