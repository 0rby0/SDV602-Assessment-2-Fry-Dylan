import FreeSimpleGUI as sg
import multiprocessing as mp

from session_manager import SessionManager

from GUI.des_window import DESWindow
from GUI.session_creator import SessionCreator

class DESSelection:
	def __init__(self, login_window):
		# Create a reference to the login window
		self.login_window = login_window

		self.is_updating = False

		self.sessions = [["None"]]
		self.windows = []

		# Create the window
		self.window = self.create_window()
		# Show the window
		self.show()
   
   
	def create_window(self):
		controls_layout = [
												[ sg.Button(button_text = "Sign Out", key = "-SIGNOUT-") ],
												[ sg.Button(button_text = "Create", key = "-CREATE-") ],
												[ sg.Button(button_text = "Delete", key = "-DELETE-") ],
												[ sg.Button(button_text = "Select", key = "-SELECT-") ]
											]

		search_layout = [
											[ sg.Text("Username", key = "-USERNAME-"), sg.Push(), sg.Input(key = "-SEARCH-") ],
											[ sg.Table(values = self.sessions, auto_size_columns = False, col_widths = [50], num_rows = 10, justification = "left", headings = ["Public Sessions"], key = "-SESSIONS-") ]
										]

		layout = [[ sg.Column(search_layout), sg.Column(controls_layout) ]]

		return sg.Window("DES Analysis App", layout = layout, finalize = True)
   
   
	def show(self):
		while True:
			event, values = self.window.read(10)
	
			if values:
				self.update_display(search_input = values["-SEARCH-"], current_selection = values["-SESSIONS-"])

			match event:
				case "-SIGNOUT-":
					# Close this window
					self.window.close()

					# Redisplay the login window
					self.login_window.window.un_hide()
					self.login_window.show()

				case "-CREATE-":
					self.window.hide()
					SessionCreator(des_selection_window = self)

				case "-DELETE-":
					pass

				case "-SELECT-":
					SessionManager().join_session(session_name = self.sessions[values["-SESSIONS-"][0]][0])

					des = DESWindow(session_name = self.sessions[values["-SESSIONS-"][0]][0])
					des_process = mp.Process(target = des.show)
					self.windows.append(des_process)
					des_process.start()

		
				case sg.WINDOW_CLOSED:
					if not self.is_updating:
						break

		self.close_window()


	def update_display(self, search_input, current_selection):
		# Lock the application from closing during an update
		self.is_updating = True
  
		if search_input is not None:
			result =  SessionManager().search_sessions(search_input)
   
			# Make sure the result is always in a list
			if isinstance(result, str):
				result = [result]
    
			# Put each element of the list into its own list for the row
			table_ready_result = []
			for entry in result:
				table_ready_result.append([entry])

			self.sessions = table_ready_result
			self.window["-SESSIONS-"].update(values = self.sessions, select_rows = current_selection)
			self.window["-USERNAME-"].update(value = SessionManager().user.username)

		self.is_updating = False


	def close_window(self):
		if self.login_window:
			self.login_window.close_window()

		self.window.close()