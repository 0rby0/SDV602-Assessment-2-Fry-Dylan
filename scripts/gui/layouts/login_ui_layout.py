import FreeSimpleGUI as sg

title = [ [sg.Text("DES Analysis App")] ]

input_layout = [
									[ sg.Text(text = "Login", key = "-HEADING-") ],
									[ sg.Text("Username"), sg.Input(key = "-USERNAME-") ],
									[ sg.Text("Password"), sg.Input(key = "-PASSWORD-") ],
									[ sg.Button(button_text = "Submit", key = "-SUBMIT-") ],
									[ sg.Button("Don't have an account? Sign Up", key = "-TOGGLE-") ]
								]

layout = [
					[ sg.Column(title), sg.Column(input_layout) ]
				]
