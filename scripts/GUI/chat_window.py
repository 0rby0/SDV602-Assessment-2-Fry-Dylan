import FreeSimpleGUI as sg

class ChatWindow:
	def __init__(self, session):
		self.session = session

		# Create the window
		self.window = self.create_window()
   
   
	def create_window(self):
		layout = [
							[ sg.Text(self.session_name, size = (40, 1), justification = "center") ],
							[ sg.HorizontalSeparator() ],
							[ sg.Multiline(size = (47, 25), disabled = True, key = "-CHATLOG-") ],
							[ sg.Input(key = "-MESSAGEINPUT-"), sg.Button(">", key = "-SUBMIT-") ]
						]

		return sg.Window("DES Analysis App", layout = layout, disable_close = True)
   
   
	def show(self):
		while True:
			event, values = self.window.read(10)

			self.window["-CHATLOG-"].update(self.session.get_messages())

			match event:
				case "-SUBMIT-":
					self.app.session.send_message(self.app.user, values["-MESSAGEINPUT-"])


	def close_window(self):
		self.window.close()