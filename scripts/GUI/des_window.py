import FreeSimpleGUI as sg

from session_manager import SessionManager

from GUI.data_source_manager import DataSourceManager
from GUI.des_config import DESConfig

class DESWindow:
	def __init__(self, session_name):
		self.session = SessionManager().get_session_by_name(session_name)

		self.children = []

		# Create the window
		self.window = self.create_window()

   
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
				case "-MANAGE-":
					self.window.hide()
					DataSourceManager(des_window = self, session_name = self.session.session_name)

				case "-CONFIGURE-":
					pass

				case sg.WINDOW_CLOSED:
					break
		
		self.close_window()


	def close_window(self):
		for child in self.children:
			child.close_window()

		self.window.close()