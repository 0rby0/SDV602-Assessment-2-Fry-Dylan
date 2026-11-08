import FreeSimpleGUI as sg
class SessionCreatorUILayout:
	def __init__(self):
		self.layout = [
					[ sg.Text("Create Session") ],
					[ sg.Text("Session Name"), sg.Input(key = "-SESSIONNAME-") ],
					[ sg.Button(button_text = "Cancel", key = "-CANCEL-"), sg.Checkbox(text = "Public", key = "-PUBLICTOGGLE-"), sg.Button(button_text = "Create", key = "-SUBMIT-") ]
				]

	def terminate(self):
		self.layout = None
  