import FreeSimpleGUI as sg

from gui.layouts.data_manager_ui_layout import DataManagerUILayout

def parse(session_manager, session_name, des_window):
	layout = DataManagerUILayout()
	window = sg.Window(title = "Manage Data", layout = layout.layout)

	session = session_manager.get_session_by_name(session_name)

	while True:
		event, values = window.read(10)

		selected_set = [0]
		selected_source = [0]
		if values:
			if len(values["-DATASETS-"]) > 0:
				selected_set = values["-DATASETS-"]
				
			if len(values["-DATASOURCES-"]) > 0:
				selected_source = values["-DATASOURCES-"]

			update_display(window = window, session_manager = session_manager, session_name = session_name, current_set_selection = selected_set, current_source_selection = selected_source)

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
				session.display.data_conf.update_dataset(session.compile_dataset(session._files.datasets[values["-DATASETS-"][0]]))
				break
			
			case sg.WINDOW_CLOSED:
				close_tree(des_window = des_window)
				break

	window.close()
	layout.terminate()


def close_tree(des_window):
	des_window.write_event_value(sg.WIN_CLOSED, None)


def update_display(window, session_manager, session_name, current_set_selection, current_source_selection):
	session = session_manager.get_session_by_name(session_name)

	result_1 = session._files.get_data_sets()

	# Make sure the result is always in a list
	if isinstance(result_1, str):
		result_1 = [result_1]

	# Put each element of the list into its own list for the row
	table_ready_result_1 = []
	for entry in result_1:
		table_ready_result_1.append([entry])

	window["-DATASETS-"].update(values = table_ready_result_1, select_rows = current_set_selection)


	result_2 = session._files.get_data_sources(session._files.get_data_sets()[current_set_selection[0]])

	# Make sure the result is always in a list
	if isinstance(result_2, str):
		result_2 = [result_2]

	# Put each element of the list into its own list for the row
	table_ready_result_2 = []
	for entry in result_2:
		table_ready_result_2.append([entry])

	if session._files.get_data_sets() != "No datasets": 
		window["-DATASETNAME-"].update(value = session._files.datasets[current_set_selection[0]])
		window["-DATASOURCES-"].update(values = table_ready_result_2, select_rows = current_source_selection)
