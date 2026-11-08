import FreeSimpleGUI as sg

class DataManagerUILayout:
	def __init__(self):
		self.source_layout = [
											[ sg.Text(text = "Dataset Name", key = "-DATASETNAME-") ],
											[ sg.Table(values = [["None"]], auto_size_columns = False, col_widths = [30], justification = "left", key = "-DATASOURCES-") ]
										]

		self.controls_layout = [
											[ sg.Button(button_text = "New Source", key = "-ADDSOURCE-") ],
											[ sg.Button(button_text = "Remove Source", key = "-REMOVESOURCE-") ],
											[ sg.FileBrowse(button_text = "Append Source", file_types = (("CSV Files", "*.csv"),), enable_events = True, key = "-APPENDSOURCE-") ],
											[ sg.Button(button_text = "Remove Append", key = "-REMOVEAPPENDED-") ],
											[ sg.VPush() ],
											[ sg.Button(button_text = "Load Source", key = "-SELECT-") ]
											]

		self.layout = [
							[ sg.Table(values = [["None"]], auto_size_columns = False, col_widths = [30], justification = "left", key = "-DATASETS-"), sg.Column(self.source_layout), sg.Column(self.controls_layout) ]
						]

	def terminate(self):
		self.source_layout = None
		self.controls_layout = None
		self.layout = None



