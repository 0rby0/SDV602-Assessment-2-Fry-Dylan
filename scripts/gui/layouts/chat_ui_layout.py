import FreeSimpleGUI as sg

layout = [
					[ sg.Text("Session Name", size = (40, 1), justification = "center") ],
					[ sg.HorizontalSeparator() ],
					[ sg.Multiline(size = (47, 25), disabled = True, key = "-CHATLOG-") ],
					[ sg.Input(key = "-MESSAGEINPUT-"), sg.Button(">", key = "-SUBMIT-") ]
				]
