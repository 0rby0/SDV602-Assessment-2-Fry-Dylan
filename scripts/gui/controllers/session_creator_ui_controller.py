import FreeSimpleGUI as sg

from gui.layouts.session_creator_ui_layout import layout


def parse(session_manager, browser_window):
	window = sg.Window(title = "Session Creator", layout = layout)

	result = None

	while True:
		event, values = window.read()

		match event:
				case "-SUBMIT-":
					result = session_manager.create_session(session_name = values["-SESSIONNAME-"], public = values["-PUBLICTOGGLE-"], redirect = False)
					break

				case sg.WINDOW_CLOSED | "-CANCEL-":
					close_tree(window = window, browser_window = browser_window)

	window.close()
	return result


def close_tree(window, browser_window):
	browser_window.write_event_value(sg.WINDOW_CLOSED, None)
	window.close()