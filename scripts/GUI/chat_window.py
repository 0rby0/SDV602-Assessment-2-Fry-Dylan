import FreeSimpleGUI as sg

from session_manager import SessionManager

class ChatWindow:
	def __init__(self, session_name):
		self.session_name = session_name

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
		session = SessionManager().get_session_by_name(self.session_name)

		while True:
			event, values = self.window.read(10)

			if session: # TEMP CRASH FIX
				self.window["-CHATLOG-"].update(session.get_messages())

			match event:
				case "-SUBMIT-":
					if session: # TEMP CRASH FIX
						session.send_message(SessionManager().user, values["-MESSAGEINPUT-"])


	def close_window(self):
		self.window.close()