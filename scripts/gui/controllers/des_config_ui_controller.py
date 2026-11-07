import FreeSimpleGUI as sg

from gui.layouts.des_config_ui_layout import layout


def parse(session_manager, session_name, des_window):
	des_window.disable()
	window = sg.Window(title = "Configure", layout = layout, disable_close = True)

	initial_values = session_manager.get_session_by_name(session_name).display.data_conf.get_settings()

	while True:
		event, values = window.read(10)

		settings = session_manager.get_session_by_name(session_name).display.data_conf.get_settings()

		try:
			y_index = settings["y"]["options"].index(y_selection = values["-YSELECT-"])
		except:
			y_index = 0

		try:
			x_index = settings["x"]["options"].index(values["-XSELECT-"])
		except:
			x_index = 0

		try:
			series_index = settings["series"]["options"].index(values["-LEGENDSELECT-"])
		except:
			series_index = 0

		try:
			get_index = settings["get"]["options"].index(values["-SUBLEGENDSELECT-"])
		except:
			get_index = 0

		window["-YSELECT-"].update(values = settings["y"]["options"], set_to_index = y_index)
		window["-XSELECT-"].update(values = settings["x"]["options"], set_to_index = x_index)
		window["-LEGENDSELECT-"].update(values = settings["series"]["options"], set_to_index = series_index)
		window["-SUBLEGENDSELECT-"].update(values = settings["get"]["options"], set_to_index = get_index)

		# Update the data display
		session_manager.get_session_by_name(session_name).display.data_conf.change_setting("x", values["-XSELECT-"])
		session_manager.get_session_by_name(session_name).display.data_conf.change_setting("y", values["-YSELECT-"])
		session_manager.get_session_by_name(session_name).display.data_conf.change_setting("series", values["-LEGENDSELECT-"])
		session_manager.get_session_by_name(session_name).display.data_conf.change_setting("get", values["-SUBLEGENDSELECT-"])

		match event:
			case "-SUBMIT-":
				session_manager.get_session_by_name(session_name).display.data_conf.graph_type = values["-TYPESELECT-"]
				break

	des_window.enable()
	window.close()