import FreeSimpleGUI as sg
import multiprocessing as mp

from gui.layouts.des_ui_layout import layout
from gui.controllers.data_manager_ui_controller import parse as parse_manager
from gui.controllers.chat_ui_controller import parse as parse_chat
from gui.controllers.des_config_ui_controller import parse as parse_config

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def draw_figure(window, graph_canvas, toolbar_canvas, figure):
	if not hasattr(draw_figure, 'current_canvas_agg'):
		draw_figure.current_canvas_agg = None

	# Clear the canvas
	if draw_figure.current_canvas_agg:
		old_widget = draw_figure.current_canvas_agg.get_tk_widget()
		old_widget.forget()
		old_widget.destroy()
		draw_figure.current_canvas_agg = None

	# Clear the toolbar
	toolbar_tk_canvas = toolbar_canvas.TKCanvas
	for child in toolbar_tk_canvas.winfo_children():
		child.destroy()

	figure_canvas_agg = FigureCanvasTkAgg(figure, graph_canvas)
	figure_canvas_agg.draw()

	widget = figure_canvas_agg.get_tk_widget()
	widget.pack(side = "top", fill = "both", expand = 1)

	toolbar_canvas_agg = toolbar_canvas.TKCanvas
	toolbar = NavigationToolbar2Tk(figure_canvas_agg, toolbar_canvas_agg)
	toolbar.update()

	draw_figure.current_canvas_agg = figure_canvas_agg

	figure_canvas_agg.get_tk_widget().pack(side = "top", fill = "both", expand = 1)

	return figure_canvas_agg


def load_graph(window, session):
	data_display = session.display

	tk_root = window.TKroot
	sys_dpi = tk_root.winfo_fpixels("1i") / 2

	fig, ax = plt.subplots(figsize=(8, 6), dpi = sys_dpi)

	if data_display.data_conf.data:
		match data_display.data_conf.graph_type:
			case "Line":
				fig = data_display.generate_chart_line(sys_dpi)

			case "Bar":
				fig = data_display.generate_chart_bar(sys_dpi)

			case "Pie":
				fig = data_display.generate_chart_pie(sys_dpi)

			case _:
				fig = None

	else:
		ax.text(0.5, 0.5, "No Dataset Loaded", horizontalalignment="center", verticalalignment = "center", fontsize = 12)
		ax.set_axis_off()

	if fig:
		draw_figure(window, window["-GRAPHDISPLAY-"].TKCanvas, window["-GRAPHCONTROLS-"], fig)


def parse(session_manager, session_name):
	window = sg.Window(title = "DES Analysis App", layout = layout, finalize = True)

	refresh_graph = load_graph

	chat_window = None
	if session_manager.get_session_by_name(session_name).creator is not None:
		chat_window = mp.Process(target = parse_chat, args = (session_manager, session_name,))
		chat_window.start()

	while True:
		event, values = window.read(30)

		match event:
			case "-MANAGE-":
				window.hide()
				parse_manager(session_manager = session_manager, session_name = session_name, des_window = window)
				window.un_hide()

			case "-CONFIGURE-":
				parse_config(session_manager = session_manager, session_name = session_name, des_window = window)

			case "-RELOADGRAPH-":
				refresh_graph(window = window, session = session_manager.get_session_by_name(session_name))

			case sg.WINDOW_CLOSED:
				session_manager.leave_session(session_name)
				break

	close_tree(window = window, chat_window = chat_window)


def close_tree(window, chat_window):
	if chat_window:
		chat_window.terminate()
	window.close()