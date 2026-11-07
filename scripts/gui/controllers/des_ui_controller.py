import FreeSimpleGUI as sg
import multiprocessing as mp

from gui.layouts.des_ui_layout import layout
from gui.controllers.data_manager_ui_controller import parse as parse_manager
from gui.controllers.chat_ui_controller import parse as parse_chat
from gui.controllers.des_config_ui_controller import parse as parse_config

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_figure(canvas, figure):
	if not hasattr(draw_figure, 'canvas_packed'):
		draw_figure.canvas_packed = {}

	figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
	figure_canvas_agg.draw()

	widget = figure_canvas_agg.get_tk_widget()
	if widget not in draw_figure.canvas_packed:
		draw_figure.canvas_packed[widget] = figure
		widget.pack(side = "top", fill = "both", expand = 1)

	return figure_canvas_agg


def delete_figure_agg(figure_agg):
	figure_agg.get_tk_widget().forget()

	draw_figure.canvas_packed.pop(figure_agg.get_tk_widget())

	plt.close("all")


def load_graph(window, session):
	data_display = session.display

	fig, ax = plt.subplots(figsize=(8, 6))
	if data_display.data_conf.data:
		match data_display.data_conf.graph_type:
			case "Line":
				fig = data_display.generate_chart_line()

			case "Bar":
				fig = data_display.generate_chart_bar()

			case "Pie":
				fig = data_display.generate_chart_pie()

			case _:
				fig = None

	else:
		ax.text(0.5, 0.5, "No Dataset Loaded", horizontalalignment="center", verticalalignment = "center", fontsize = 12)
		ax.set_axis_off()

	if fig:
		draw_figure(window["-GRAPHDISPLAY-"].TKCanvas, fig)


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