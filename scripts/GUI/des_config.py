import FreeSimpleGUI as sg

from session_manager import SessionManager

class DESConfig:
	def __init__(self, session_name, des_window):
		self.session = SessionManager().get_session_by_name(session_name)
		self.des_window = des_window

		# Create the window
		self.window = self.create_window()
		# Show the window
		self.show()
   
   
	def create_window(self):
		initial_settings = SessionManager().data_display.data_conf.get_settings()

		layout = [
							[ sg.Text("Type"), sg.Combo(values = ["Line", "Pie", "Bar"], default_value = "Line", key = "-TYPESELECT-") ],
							[ sg.Text("Y Key"), sg.Combo(values = initial_settings["y"]["options"], default_value = initial_settings["y"]["selected"], key = "-YSELECT-") ],
							[ sg.Text("X Key"), sg.Combo(values = initial_settings["x"]["options"], default_value = initial_settings["x"]["selected"], key = "-XSELECT-") ],
							[ sg.Text("Legend"), sg.Combo(values = initial_settings["series"]["options"], default_value = initial_settings["series"]["selected"], key = "-LEGENDSELECT-") ],
							[ sg.Text("Legend Series"), sg.Combo(values = initial_settings["get"]["options"], default_value = initial_settings["get"]["selected"], key = "-SUBLEGENDSELECT-") ],
							[ sg.Button(button_text = "Cancel", key = "-CANCEL-"), sg.Button(button_text = "Submit", key = "-SUBMIT-") ]
						]

		return sg.Window("DES Analysis App", layout = layout)
   
   
	def show(self):
		while True:
			event, values = self.window.read(10)

			settings = SessionManager().data_display.data_conf.get_settings()

			self.window["-YSELECT-"].update(values = settings["y"]["options"])
			self.window["-XSELECT-"].update(values = settings["x"]["options"])
			self.window["-LEGENDSELECT-"].update(values = settings["series"]["options"])
			self.window["-SUBLEGENDSELECT-"].update(values = settings["get"]["options"])

			match event:
				case "-SUBMIT-":
					SessionManager().data_display.data_conf.graph_type = values["-TYPESELECT-"]
					SessionManager().data_display.data_conf.change_setting("x", values["-XSELECT-"])
					SessionManager().data_display.data_conf.change_setting("y", values["-YSELECT-"])
					SessionManager().data_display.data_conf.change_setting("series", values["-LEGENDSELECT-"])
					SessionManager().data_display.data_conf.change_setting("get", values["-SUBLEGENDSELECT-"])
					self.des_window.load_graph()
					self.window.close()

				case sg.WINDOW_CLOSED | "-CANCEL-":
					break

				case _:
					pass

		self.close_window()


	def close_window(self):
		self.window.close()