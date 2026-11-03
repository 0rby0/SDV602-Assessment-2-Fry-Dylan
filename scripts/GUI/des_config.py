import FreeSimpleGUI as sg

class DESConfig:
	def __init__(self, app):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app
		self.app = app

		# Show the window
		self.show()
   
   
	def create_window(self):
		layout = [
							[ sg.Text("Type"), sg.Combo(values = ["Line", "Pie", "Bar"], key = "-TYPESELECT-") ],
							[ sg.Text("Y Key"), sg.Combo(values = ["None"], key = "-YSELECT-") ],
							[ sg.Text("X Key"), sg.Combo(values = ["None"], key = "-XSELECT-") ],
							[ sg.Text("Legend"), sg.Combo(values = ["None"], key = "-LEGENDSELECT-") ],
							[ sg.Text("Legend Series"), sg.Combo(values = ["None"], key = "-SUBLEGENDSELECT-") ],
							[ sg.Button(button_text = "Cancel", key = "-CANCEL-"), sg.Button(button_text = "Submit", key = "-SUBMIT-") ]
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