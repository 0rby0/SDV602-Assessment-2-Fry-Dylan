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
					break

				case sg.WINDOW_CLOSED | "-CANCEL-":
					break

	browser_window.un_hide()
	window.close()
		