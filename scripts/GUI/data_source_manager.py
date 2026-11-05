import FreeSimpleGUI as sg

from session_manager import SessionManager

class DataSourceManager:
	def __init__(self, des_window, session_name):
		# A reference back to the DES window for switching back
		self.des_window = des_window

		# The name of the session that this is managing
		self.session_name = session_name

		# Create the window
		self.window = self.create_window()
		# Show the window
		self.show()
  
  
	def create_window(self):
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

		return sg.Window("DES Analysis App", layout = layout)
  
  
	def show(self):
		session = SessionManager().get_session_by_name(self.session_name)

		while True:
			event, values = self.window.read(10)

			if values:
				selected_set = [0]
				if len(values["-DATASETS-"]) > 0:
					selected_set = values["-DATASETS-"]

					
				selected_source = [0]
				if len(values["-DATASOURCES-"]) > 0:
					selected_source = values["-DATASOURCES-"]

				self.update_display(selected_set, selected_source)

			match event:
				case "-ADDSOURCE-":
					name_window = sg.Window("New Dataset Name", disable_close = True, layout = [[sg.Input(key = "-DATASETNAMEENTRY-")], [sg.Button("Cancel", key = "-CANCEL-"), sg.Button("Confirm", key = "-CONFIRM-")]])
					
					while True:
						events, values = name_window.read()
						if events == "-CONFIRM-":
							session.new_dataset(values["-DATASETNAMEENTRY-"])
							break
						else:
							break
					name_window.close()

				case "-REMOVESOURCE-":
					if values["-DATASETS-"]:
						session.remove_dataset(session._files.get_data_sets()[selected_set[0]])

				case "-APPENDSOURCE-":
					if values["-DATASETS-"] and session._files.get_data_sets() != "No datasets":
						session.add_datasource(values["-APPENDSOURCE-"], session._files.get_data_sets()[selected_set[0]])

				case "-REMOVEAPPENDED-":
					if values["-DATASOURCES-"] and session._files.get_data_sources(session._files.datasets[selected_set[0]]) != "Dataset not found":
						session.remove_datasource(session._files.get_data_sources(session._files.datasets[selected_set[0]])[selected_source[0]], session._files.datasets[selected_set[0]])

				case "-SELECT-":
					# Don't try to exit if nothing is selected
					if values["-DATASETS-"] == [] or session._files.get_data_sets() == "No datasets": return

					# Update the DES screen to be using the selected dataset
					SessionManager().data_display.data_conf.update_dataset(session.compile_dataset(session._files.datasets[values["-DATASETS-"][0]]))

					# Show the DES screen and close this window
					self.window.close()
					self.des_window.window.un_hide()
					self.des_window.show()

				case sg.WINDOW_CLOSED:
					break

		self.close_window()


	def update_display(self, current_set_selection, current_source_selection):
		session = SessionManager().get_session_by_name(self.session_name)

		result_1 = session._files.get_data_sets()

		# Make sure the result is always in a list
		if isinstance(result_1, str):
			result_1 = [result_1]

		# Put each element of the list into its own list for the row
		table_ready_result_1 = []
		for entry in result_1:
			table_ready_result_1.append([entry])

		self.window["-DATASETS-"].update(values = table_ready_result_1, select_rows = current_set_selection)


		result_2 = session._files.get_data_sources(session._files.get_data_sets()[current_set_selection[0]])

		# Make sure the result is always in a list
		if isinstance(result_2, str):
			result_2 = [result_2]

		# Put each element of the list into its own list for the row
		table_ready_result_2 = []
		for entry in result_2:
			table_ready_result_2.append([entry])

		if session._files.get_data_sets() != "No datasets": 
			self.window["-DATASETNAME-"].update(value = session._files.datasets[current_set_selection[0]])
			self.window["-DATASOURCES-"].update(values = table_ready_result_2, select_rows = current_source_selection)


	def close_window(self):
		if self.des_window:
			self.des_window.close_window()

		self.window.close()