import FreeSimpleGUI as sg

from gui.layouts.des_browser_ui_layout import layout


def parse(session_manager):
	window = sg.Window(title = "Session Browser", layout = layout)
	sessions = []

	while True:
		event, values = window.read(10)

		if values:
			sessions = update_display(window = window, session_manager = session_manager, search_input = values["-SEARCH-"], current_selection = values["-SESSIONS-"])

		match event:
			case "-SIGNOUT-":
				# Close this window
				window.close()

				# Redisplay the login window

				# login_window.window.un_hide()
				# login_window.show()

			case "-CREATE-":
				window.hide()
				# SessionCreator(des_selection_window = self)

			case "-DELETE-":
				pass

			case "-SELECT-":
				session_manager.join_session(session_name = sessions[values["-SESSIONS-"][0]][0])

				# des = DESWindow(session_name = sessions[values["-SESSIONS-"][0]][0])
				# des_process = mp.Process(target = des.show)
				# windows.append(des_process)
				# des_process.start()

	
			case sg.WINDOW_CLOSED:
				break

	window.close()


def update_display(window, session_manager, search_input, current_selection):
	if search_input is not None:
		result =  session_manager.search_sessions(search_input)

		# Make sure the result is always in a list
		if isinstance(result, str):
			result = [result]

		# Put each element of the list into its own list for the row
		table_ready_result = []
		for entry in result:
			table_ready_result.append([entry])

		window["-SESSIONS-"].update(values = table_ready_result, select_rows = current_selection)
		window["-USERNAME-"].update(value = session_manager.user.username)
		return table_ready_result

