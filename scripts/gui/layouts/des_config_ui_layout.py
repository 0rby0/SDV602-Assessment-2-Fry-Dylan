import FreeSimpleGUI as sg
class DESConfigUILayout:
	def __init__(self):
		self.layout = [
					[ sg.Text("Type"), sg.Combo(values = ["Line", "Pie", "Bar"], default_value = "Line", key = "-TYPESELECT-") ],
					[ sg.Text("Y Key"), sg.Combo(values = [[]], key = "-YSELECT-") ],
					[ sg.Text("X Key"), sg.Combo(values = [[]], key = "-XSELECT-") ],
					[ sg.Text("Legend"), sg.Combo(values = [[]], key = "-LEGENDSELECT-") ],
					[ sg.Text("Legend Series"), sg.Combo(values = [[]], key = "-SUBLEGENDSELECT-") ],
					[ sg.Button(button_text = "Submit", key = "-SUBMIT-") ]
				]

	def terminate(self):
		self.layout = None
  

