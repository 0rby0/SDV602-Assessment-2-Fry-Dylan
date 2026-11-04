import FreeSimpleGUI as sg

class DataSourceManager:
	def __init__(self, des_window, session):
		self.des_window = des_window

		self.session = session

		# Create the window
		self.window = self.create_window()
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
			event, values = self.window.read(10)

			if values:
				datasets = self.session._files.datasets
				datasources = self.session._files.get_data_sources(values["-DATASETS-"])

				self.window["-DATASETS-"].update(values = datasets)
				self.window["-DATASETNAME-"].update(value = values["-DATASETS-"])
				self.window["-DATASOURCES-"].update(values = datasources)

			match event:
				case "-ADDSOURCE-":
					pass

				case "-REMOVESOURCE":
					pass

				case "-APPENDSOURCE-":
					pass

				case "-REMOVEAPPENDED-":
					pass

				case "-SELECT-":
					# Update the DES screen to be using the selected dataset
					self.app.data_display.data_conf.update_dataset(self.session.compile_dataset(values["-DATASETS-"]))

					# Show the DES screen and close this window
					self.des_window.un_hide()
					self.window.close()

				case sg.WINDOW_CLOSED:
					break

		self.close_window()


	def close_window(self):
		if self.des_window:
			self.des_window.close_window()

		self.window.close()