import FreeSimpleGUI as sg

class DataSourceManager:
	def __init__(self, app):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app
		self.app = app

		# Show the window
		self.show()
  
  
	def create_window(self):
		source_layout = [
											[ sg.Text(text = "Dataset Name", key = "-DATASETNAME-") ],
											[ sg.Table(values = [["None"]], key = "-DATASOURCES-") ]
										]

		controls_layout = [
											[ sg.Button(button_text = "New Source", key = "-ADDSOURCE-") ],
											[ sg.Button(button_text = "Remove Source", key = "-REMOVESOURCE-") ],
											[ sg.Button(button_text = "Append Source", key = "-APPENDSOURCE-") ],
											[ sg.Button(button_text = "Remove Append", key = "-REMOVEAPPENDED-") ],
											[ sg.VPush() ],
											[ sg.Button(button_text = "Load Source", key = "-SELECT-") ]
											]

		layout = [
							[ sg.Table(values = [["None"]], key = "-DATASETS-"), sg.Column(source_layout), sg.Column(controls_layout) ]
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

		self.window.close()