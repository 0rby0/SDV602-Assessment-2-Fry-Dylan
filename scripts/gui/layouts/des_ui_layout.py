import FreeSimpleGUI as sg

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

layout_column_1 = [
											[ sg.Canvas(size = (600, 400), expand_x = True, expand_y = True, key = "-GRAPHDISPLAY-"), sg.Button(button_text = "Reload", key = "-RELOADGRAPH-") ],
											[ sg.Canvas(size = (600, 50), expand_x = True, expand_y = True, key = "-GRAPHCONTROLS-") ]
									]

layout_column_2 = [
											[ sg.Text(text = "Mode", key = "-APPMODE-"), sg.Button(button_text = "Configure", key = "-CONFIGURE-") ],
											[ sg.Text(text = "Data source name", key = "-DATASETDETAILS-") ],
											[ sg.Button(button_text = "Manage Data Sources", key = "-MANAGE-") ],
											[ sg.Multiline(key = "-GRAPHDESCRIPTION-") ]
									]

layout = [
					[ sg.Column(layout = layout_column_1) ],
					[ sg.Column(layout = layout_column_2) ]
				]
