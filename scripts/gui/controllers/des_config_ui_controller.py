import FreeSimpleGUI as sg

from gui.layouts.des_config_ui_layout import layout


def parse(session_manager):
	window = sg.Window(title = "Configure", layout = layout)

	while True:
		event, values = window.read(10)

		settings = session_manager.data_display.data_conf.get_settings()

		window["-YSELECT-"].update(values = settings["y"]["options"])
		window["-XSELECT-"].update(values = settings["x"]["options"])
		window["-LEGENDSELECT-"].update(values = settings["series"]["options"])
		window["-SUBLEGENDSELECT-"].update(values = settings["get"]["options"])

		match event:
			case "-SUBMIT-":
				session_manager.data_display.data_conf.graph_type = values["-TYPESELECT-"]
				session_manager.data_display.data_conf.change_setting("x", values["-XSELECT-"])
				session_manager.data_display.data_conf.change_setting("y", values["-YSELECT-"])
				session_manager.data_display.data_conf.change_setting("series", values["-LEGENDSELECT-"])
				session_manager.data_display.data_conf.change_setting("get", values["-SUBLEGENDSELECT-"])
				# des_window.load_graph()

			case sg.WINDOW_CLOSED | "-CANCEL-":
				break

	window.close()