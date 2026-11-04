import FreeSimpleGUI as sg

class DESConfig:
	def __init__(self, app):
		# Create the window
		self.window = self.create_window()

		# Create a permanent reference to the app
		self.app = app

		# Show the window
		self.show()
   
   
	def create_window(self):
		initial_settings = self.app.data_display.data_conf.get_settings()

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

			settings = self.app.data_display.data_conf.get_settings()

			self.window["-YSELECT-"].update(values = settings["y"]["options"])
			self.window["-XSELECT-"].update(values = settings["x"]["options"])
			self.window["-LEGENDSELECT-"].update(values = settings["series"]["options"])
			self.window["-SUBLEGENDSELECT-"].update(values = settings["get"]["options"])

			match event:
				case "-SUBMIT-":
					self.app.data_display.data_conf.change_setting("x", values["-XSELECT-"])
					self.app.data_display.data_conf.change_setting("y", values["-YSELECT-"])
					self.app.data_display.data_conf.change_setting("series", values["-LEGENDSELECT-"])
					self.app.data_display.data_conf.change_setting("get", values["-SUBLEGENDSELECT-"])

				case sg.WINDOW_CLOSED | "-CANCEL-":
					break

				case _:
					pass

		self.close_window()


	def close_window(self):
		self.window.close()