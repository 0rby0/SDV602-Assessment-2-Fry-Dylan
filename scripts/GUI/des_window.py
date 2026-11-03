import FreeSimpleGUI as sg

class DESWindow:
	def __init__(self, app):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app
		self.app = app

		# Show the window
		self.show()
   
   
	def create_window(self):
		layout_column_1 = [
													[ sg.Graph(canvas_size = (100, 100), graph_bottom_left = (100, 100), graph_top_right = (0, 0), key = "-GRAPHDISPLAY-") ],
													[ sg.Graph(canvas_size = (100, 10), graph_bottom_left = (100, 10), graph_top_right = (0, 0), key = "-GRAPHCONTROLS-") ]
											]

		layout_column_2 = [
													[ sg.Text(text = "Mode", key = "-APPMODE-"), sg.Button(button_text = "Configure", key = "-CONFIGURE-") ],
													[ sg.Multiline(disabled = True, key = "-DATASETDETAILS-") ],
													[ sg.Button(button_text = "Manage Data Sources", key = "-MANAGE-") ],
													[ sg.Multiline(disabled = True, key = "-GRAPHDESCRIPTION-") ]
											]

		layout = [
							[ sg.Column(layout = layout_column_1) ],
							[ sg.Column(layout = layout_column_2) ]
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