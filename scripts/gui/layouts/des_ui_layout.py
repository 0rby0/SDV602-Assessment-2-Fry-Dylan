import FreeSimpleGUI as sg

class DESUILayout:
	def __init__(self):
		self.layout_column_1 = [
											[ sg.Canvas(size = (800, 600), expand_x = True, expand_y = True, key = "-GRAPHDISPLAY-"), sg.Button(button_text = "Reload", key = "-RELOADGRAPH-") ],
											[ sg.Canvas(size = (800, 150), expand_x = True, expand_y = True, key = "-GRAPHCONTROLS-"), sg.Slider(range = (10, 100), default_value = 10, orientation = "vertical", key = "-SCALE-") ]
									]

		self.layout_column_2 = [
													[ sg.Text(text = "Mode", key = "-APPMODE-"), sg.Button(button_text = "Configure", key = "-CONFIGURE-") ],
													[ sg.Text(text = "Data source name", key = "-DATASETDETAILS-") ],
													[ sg.Button(button_text = "Manage Data Sources", key = "-MANAGE-") ],
													[ sg.Multiline(key = "-GRAPHDESCRIPTION-") ]
											]

		self.layout = [
							[ sg.Column(layout = self.layout_column_1) ],
							[ sg.Column(layout = self.layout_column_2) ]
						]

	def terminate(self):
		self.layout_column_1 = None
		self.layout_column_2 = None
		self.layout = None
  

