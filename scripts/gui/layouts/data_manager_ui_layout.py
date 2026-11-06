import FreeSimpleGUI as sg

source_layout = [
									[ sg.Text(text = "Dataset Name", key = "-DATASETNAME-") ],
									[ sg.Table(values = [["None"]], auto_size_columns = False, col_widths = [30], justification = "left", key = "-DATASOURCES-") ]
								]

controls_layout = [
									[ sg.Button(button_text = "New Source", key = "-ADDSOURCE-") ],
									[ sg.Button(button_text = "Remove Source", key = "-REMOVESOURCE-") ],
									[ sg.FileBrowse(button_text = "Append Source", file_types = (("CSV Files", "*.csv"),), enable_events = True, key = "-APPENDSOURCE-") ],
									[ sg.Button(button_text = "Remove Append", key = "-REMOVEAPPENDED-") ],
									[ sg.VPush() ],
									[ sg.Button(button_text = "Load Source", key = "-SELECT-") ]
									]

layout = [
					[ sg.Table(values = [["None"]], auto_size_columns = False, col_widths = [30], justification = "left", key = "-DATASETS-"), sg.Column(source_layout), sg.Column(controls_layout) ]
				]

