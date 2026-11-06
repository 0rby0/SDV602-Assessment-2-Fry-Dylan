import FreeSimpleGUI as sg

from gui.layouts.session_creator_ui_layout import layout


def parse(session_manager, browser_window):
	browser_window.hide()

	window = sg.Window(title = "Session Creator", layout = layout)

	while True:
		event, values = window.read()

		match event:
				case "-SUBMIT-":
					session_manager.create_session(session_name = values["-SESSIONNAME-"], public = values["-PUBLICTOGGLE-"], redirect = False)
					browser_window.un_hide()
					window.close()

				case sg.WINDOW_CLOSED | "-CANCEL-":
					break

	close_tree(window = window, browser_window = browser_window)


def close_tree(window, browser_window):
	browser_window.write_event_value(sg.WINDOW_CLOSED, None)
	window.close()