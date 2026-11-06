import FreeSimpleGUI as sg

layout = [
					[ sg.Text("Create Session") ],
					[ sg.Text("Session Name"), sg.Input(key = "-SESSIONNAME-") ],
					[ sg.Button(button_text = "Cancel", key = "-CANCEL-"), sg.Checkbox(text = "Public", key = "-PUBLICTOGGLE-"), sg.Button(button_text = "Create", key = "-SUBMIT-") ]
				]
