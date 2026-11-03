import FreeSimpleGUI as sg
from GUI.des_window import DESWindow
from GUI.session_creator import SessionCreator

class DESSelection:
	def __init__(self, app, login_window):
		# Create the window
		self.window = self.create_window()
		self.login_window = login_window

		# Create a permanent reference to the app and update switch
		self.app = app
		self.is_updating = False

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
								[ sg.Table(values = [["None"]], auto_size_columns = False, col_widths = [50], num_rows = 10, justification = "left", headings = ["Public Sessions"], key = "-SESSIONS-") ]
						]

		layout = [
								[ sg.Column(search_layout), sg.Column(controls_layout) ]
						]

		return sg.Window("DES Analysis App", layout = layout, finalize = True)
   
   
	def show(self):
		while True:
				event, values = self.window.read(10)
    
				if values:
					self.update_display(search_input = values["-SEARCH-"], current_selection = values["-SESSIONS-"])

				match event:
					case "-SIGNOUT-":
						# Redisplay the login window
						self.login_window.un_hide()
						# Close this window
						break
   
					case "-CREATE-":
						self.window.hide()
						SessionCreator(self.app)
						break
   
					case "-DELETE-":
						pass
   
					case "-SELECT-":
						self.window.hide()
						DESWindow(self.app)
						break
       
					case sg.WINDOW_CLOSED:
						if not self.is_updating:
							# Close the login and session selection window
							self.login_window.close()
							break

					case _:
						pass

		self.window.close()

	def update_display(self, search_input, current_selection):
		# Lock the application from closing during an update
		self.is_updating = True
  
		if search_input is not None:
			result =  self.app.sm.search_sessions(search_input)
   
			# Make sure the result is always in a list
			if isinstance(result, str):
				result = [result]
    
			# Put each element of the list into its own list for the row
			table_ready_result = []
			for entry in result:
				table_ready_result.append([entry])
			
			self.window["-SESSIONS-"].update(values = table_ready_result, select_rows = current_selection)
			self.window["-USERNAME-"].update(value = self.app.user.username)

		self.is_updating = False