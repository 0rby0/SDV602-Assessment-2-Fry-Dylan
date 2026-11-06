import FreeSimpleGUI as sg
import multiprocessing as mp

from gui.layouts.des_ui_layout import layout
from gui.controllers.data_manager_ui_controller import parse as parse_manager
from gui.controllers.chat_ui_controller import parse as parse_chat
from gui.controllers.des_config_ui_controller import parse as parse_config

# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# def draw_figure(canvas, figure):
# 	if hasattr(self, "canvas_agg") and canvas_agg is not None:
# 		old_fig = canvas_agg.figure
# 		canvas_agg.get_tk_widget().forget()
# 		plt.close(old_fig)

# 	# Get the canvas
# 	tk_canvas = canvas.TKCanvas

# 	# Clear the canvas
# 	for widget in tk_canvas.winfo_children():
# 		widget.destroy()

# 	figure_canvas_agg = FigureCanvasTkAgg(figure, tk_canvas)
# 	figure_canvas_agg.draw()
# 	figure_canvas_agg.get_tk_widget().pack(side = "top", fill = "both", expand = 1)
	
# 	return figure_canvas_agg


# def load_graph(window, session):
# 	data_display = session.data_display

# 	fig, ax = plt.subplots(figsize=(8, 6))
# 	if data_display.data_conf.data:
# 		match data_display.data_conf.graph_type:
# 			case "line":
# 				fig = data_display.generate_chart_line()

# 			case "bar":
# 				fig = data_display.generate_chart_bar()

# 			case "pie":
# 				fig = data_display.generate_chart_pie()

# 			case _:
# 				fig = None

# 	else:
# 		ax.text(0.5, 0.5, "No Dataset Loaded", horizontalalignment="center", verticalalignment = "center", fontsize = 12)
# 		ax.set_axis_off()

# 	if fig:
# 		draw_figure(window["-GRAPHDISPLAY-"], fig)


def parse(session_manager, session_name):
	window = sg.Window(title = "DES Analysis App", layout = layout)

	chat_window = None
	if session_manager.get_session_by_name(session_name).creator is not None:
		chat_window = mp.Process(target = parse_chat, args = (session_manager, session_name,))
		chat_window.start()

	while True:
		event, values = window.read(30)

		match event:
			case "-MANAGE-":
				parse_manager(session_manager = session_manager, session_name = session_name, des_window = window)

			case "-CONFIGURE-":
				parse_config(session_manager = session_manager, session_name = session_name, des_window = window)

			case "-RELOADGRAPH-":
				# load_graph(window = window, session = session)
				pass

			case sg.WINDOW_CLOSED:
				session_manager.leave_session(session_name)
				break

	close_tree(window = window, chat_window = chat_window)


def close_tree(window, chat_window):
	if chat_window:
		chat_window.terminate()
	window.close()