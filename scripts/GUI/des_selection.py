import FreeSimpleGUI as sg

class DESSelection:
	def __init__(self, app):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app
		self.app = app

		# Show the window
		self.show()
   
   
	def create_window(self):
		controls_layout = [
												[ sg.Button(button_text = "Sign Out") ],
												[ sg.Button(button_text = "Create") ],
												[ sg.Button(button_text = "Delete") ],
												[ sg.Button(button_text = "Select") ]
											]

		search_layout = [
								[ sg.Text("Username", key = "-USERNAME-"), sg.Input(key = "-SEARCH-") ],
								[ sg.Table(values = [["None"]], key = "-SESSIONS-") ]
						]

		layout = [
								[ sg.Column(search_layout), sg.Column(controls_layout) ]
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