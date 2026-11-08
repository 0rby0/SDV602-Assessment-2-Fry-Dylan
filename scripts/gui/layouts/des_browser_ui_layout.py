import FreeSimpleGUI as sg

class DESBrowserUILayout:
	def __init__(self):
		self.controls_layout = [
										[ sg.Button(button_text = "Sign Out", key = "-SIGNOUT-") ],
										[ sg.Button(button_text = "Create", key = "-CREATE-") ],
										[ sg.Button(button_text = "Delete", key = "-DELETE-") ],
										[ sg.Button(button_text = "Select", key = "-SELECT-") ]
									]

		self.search_layout = [
											[ sg.Text("Username", key = "-USERNAME-"), sg.Push(), sg.Input(key = "-SEARCH-") ],
											[ sg.Table(values = [[]], auto_size_columns = False, col_widths = [50], num_rows = 10, justification = "left", headings = ["Public Sessions"], key = "-SESSIONS-") ]
										]

		self.layout = [[ sg.Column(self.search_layout), sg.Column(self.controls_layout) ]]

	def terminate(self):
		self.controls_layout = None
		self.search_layout = None
		self.layout = None


