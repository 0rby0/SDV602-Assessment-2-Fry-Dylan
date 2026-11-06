import FreeSimpleGUI as sg

from gui.layouts.chat_ui_layout import layout


def parse(session_manager, session_name):
	window = sg.Window(title = "Session Chat", layout = layout)

	session = session_manager.get_session_by_name(session_name)

	while True:
		event, values = window.read(10)

		window["-CHATLOG-"].update(session.get_messages())

		match event:
			case "-SUBMIT-":
				session.send_message(session_manager.user, values["-MESSAGEINPUT-"])

