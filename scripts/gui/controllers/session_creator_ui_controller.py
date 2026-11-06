import FreeSimpleGUI as sg

from gui.layouts.session_creator_ui_layout import layout


def parse(session_manager):
	window = sg.Window(title = "Session Creator", layout = layout)

	while True:
		event, values = window.read()

		match event:
				case "-SUBMIT-":
					session_manager.create_session(session_name = values["-SESSIONNAME-"], public = values["-PUBLICTOGGLE-"], redirect = False)
					window.close()
					# des_selection_window.window.un_hide()
					# des_selection_window.show()

				case "-CANCEL-":
					# des_selection_window.window.un_hide()
					window.close()

				case sg.WINDOW_CLOSED:
					break

	window.close()
		