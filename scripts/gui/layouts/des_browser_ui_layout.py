import FreeSimpleGUI as sg

controls_layout = [
										[ sg.Button(button_text = "Sign Out", key = "-SIGNOUT-") ],
										[ sg.Button(button_text = "Create", key = "-CREATE-") ],
										[ sg.Button(button_text = "Delete", key = "-DELETE-") ],
										[ sg.Button(button_text = "Select", key = "-SELECT-") ]
									]

search_layout = [
									[ sg.Text("Username", key = "-USERNAME-"), sg.Push(), sg.Input(key = "-SEARCH-") ],
									[ sg.Table(values = [[]], auto_size_columns = False, col_widths = [50], num_rows = 10, justification = "left", headings = ["Public Sessions"], key = "-SESSIONS-") ]
								]

layout = [[ sg.Column(search_layout), sg.Column(controls_layout) ]]
