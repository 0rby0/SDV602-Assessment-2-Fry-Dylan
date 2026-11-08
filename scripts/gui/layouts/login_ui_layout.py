import FreeSimpleGUI as sg
class LoginUILayout:
	def __init__(self):
		self.title = [ [sg.Text("DES Analysis App")] ]

		self.input_layout = [
											[ sg.Text(text = "Login", key = "-HEADING-") ],
											[ sg.Text("Username"), sg.Input(key = "-USERNAME-") ],
											[ sg.Text("Password"), sg.Input(key = "-PASSWORD-") ],
											[ sg.Button(button_text = "Submit", key = "-SUBMIT-") ],
											[ sg.Button("Don't have an account? Sign Up", key = "-TOGGLE-") ]
										]

		self.layout = [
							[ sg.Column(self.title), sg.Column(self.input_layout) ]
						]

	def terminate(self):
		self.title = None
		self.input_layout = None
		self.layout = None

