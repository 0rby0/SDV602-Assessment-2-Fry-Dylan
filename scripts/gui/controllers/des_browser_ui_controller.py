import FreeSimpleGUI as sg
import multiprocessing as mp

from gui.layouts.des_browser_ui_layout import layout
from gui.controllers.session_creator_ui_controller import parse as parse_creator
from gui.controllers.des_ui_controller import parse as parse_des


def parse(session_manager, login_window):
	login_window.hide()

	window = sg.Window(title = "Session Browser", layout = layout)
	sessions = []
	sub_windows = []

	while True:
		event, values = window.read(10)

		if values:
			sessions = update_display(window = window, session_manager = session_manager, search_input = values["-SEARCH-"], current_selection = values["-SESSIONS-"])

		match event:
			case "-SIGNOUT-":
				login_window.un_hide()
				break

			case "-CREATE-":
				window.hide()
				new_session = parse_creator(session_manager = session_manager, browser_window = window)
				window.un_hide()
    
				if "Success" in new_session:
					idx1 = new_session.find("'")
					idx2 = new_session.find("'", idx1 + 1)
					session_name = new_session[idx1 + 1:idx2]
       
					des_process = mp.Process(target = parse_des, args = (session_manager, session_name,))
					sub_windows.append(des_process)
					des_process.start()

			case "-DELETE-":
				confirmation_window = sg.Window("Delete Session", disable_close = True, layout = [[sg.Text("Are you sure you want to delete this session?")], [sg.Button("No", key = "-NO-"), sg.Button("Yes", key = "-YES-")]])
	
				selected_session = sessions[values["-SESSIONS-"][0]][0]
    
				while True:
					events, values = confirmation_window.read()
					if events == "-YES-":
						print(selected_session)
						print(session_manager.remove_session(session_name = selected_session, user = session_manager.user))
						break
					else:
						break
				confirmation_window.close()

			case "-SELECT-":
				session_manager.join_session(session_name = sessions[values["-SESSIONS-"][0]][0])

				des_process = mp.Process(target = parse_des, args = (session_manager, sessions[values["-SESSIONS-"][0]][0],))
				sub_windows.append(des_process)
				des_process.start()
				
			case sg.WINDOW_CLOSED:
				close_tree(window = window, login_window = login_window, sub_windows = sub_windows)
				break

	window.close()


def close_tree(window, login_window, sub_windows):
	login_window.write_event_value(sg.WIN_CLOSED, None)

	for window in sub_windows:
		window.terminate()


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

