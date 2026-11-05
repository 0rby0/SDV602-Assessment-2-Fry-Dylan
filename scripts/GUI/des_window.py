import FreeSimpleGUI as sg
import multiprocessing as mp

from session_manager import SessionManager

from GUI.data_source_manager import DataSourceManager
from GUI.des_config import DESConfig
from GUI.chat_window import ChatWindow

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DESWindow:
	def __init__(self, session_name):
		self.session_name = session_name

		self.chat = None

		session = SessionManager().get_session_by_name(self.session_name)

		self.mode = "Local Mode"
		if session.db is not None:
			self.mode = "Remote Mode"

		chat = ChatWindow(self.session_name)
		chat_process = mp.Process(target = chat.show)
		self.chat = chat_process
		chat_process.start()

		# Create the window
		self.window = self.create_window()

		self.load_graph()

   
	def create_window(self):
		layout_column_1 = [
													[ sg.Canvas(size = (600, 400), expand_x = True, expand_y = True, key = "-GRAPHDISPLAY-"), sg.Button(button_text = "Reload", key = "-RELOADGRAPH-") ],
													[ sg.Canvas(size = (600, 50), expand_x = True, expand_y = True, key = "-GRAPHCONTROLS-") ]
											]

		layout_column_2 = [
													[ sg.Text(text = self.mode, key = "-APPMODE-"), sg.Button(button_text = "Configure", key = "-CONFIGURE-") ],
													[ sg.Text(text = SessionManager().data_display.data_conf.data_name, key = "-DATASETDETAILS-") ],
													[ sg.Button(button_text = "Manage Data Sources", key = "-MANAGE-") ],
													[ sg.Multiline(key = "-GRAPHDESCRIPTION-") ]
											]

		layout = [
							[ sg.Column(layout = layout_column_1) ],
							[ sg.Column(layout = layout_column_2) ]
						]

		return sg.Window("DES Analysis App", layout = layout, finalize = True)
   

	def draw_figure(self, canvas, figure):
		if hasattr(self, "canvas_agg") and self.canvas_agg is not None:
			old_fig = self.canvas_agg.figure
			self.canvas_agg.get_tk_widget().forget()
			plt.close(old_fig)

		# Get the canvas
		tk_canvas = canvas.TKCanvas

		# Clear the canvas
		for widget in tk_canvas.winfo_children():
			widget.destroy()

		figure_canvas_agg = FigureCanvasTkAgg(figure, tk_canvas)
		figure_canvas_agg.draw()
		figure_canvas_agg.get_tk_widget().pack(side = "top", fill = "both", expand = 1)
		
		return figure_canvas_agg


	def load_graph(self):
		data_display = SessionManager().data_display

		fig, ax = plt.subplots(figsize=(8, 6))
		if data_display.data_conf.data:
			match data_display.data_conf.graph_type:
				case "line":
					fig = data_display.generate_chart_line()

				case "bar":
					fig = data_display.generate_chart_bar()

				case "pie":
					fig = data_display.generate_chart_pie()

				case _:
					fig = None

		else:
			ax.text(0.5, 0.5, "No Dataset Loaded", horizontalalignment="center", verticalalignment = "center", fontsize = 12)
			ax.set_axis_off()

		if fig:
			self.draw_figure(self.window["-GRAPHDISPLAY-"], fig)

	
	def show(self):
		while True:
			event, values = self.window.read(30)

			match event:
				case "-MANAGE-":
					self.window.hide()
					DataSourceManager(des_window = self, session_name = self.session_name)

				case "-CONFIGURE-":
					DESConfig(self.session_name, des_window = self)

				case "-RELOADGRAPH-":
					self.load_graph()

				case sg.WINDOW_CLOSED:
					break
		
		self.close_window()


	def close_window(self):
		if self.chat:
			self.chat.terminate()

		self.window.close()