import FreeSimpleGUI as sg

class SessionCreator:
    def show(self):
        layout = [
                        [ sg.Text("Create Session") ],
                        [ sg.Text("Session Name"), sg.Input(key = "-SESSIONNAME-") ],
                        [ sg.Button(button_text = "Cancel", key = "-CANCEL-"), sg.Checkbox(text = "Public", key = "-PUBLICTOGGLE-"), sg.Button(button_text = "Create", key = "-SUBMIT-") ]
                    ]

        window = sg.Window("DES Analysis App", layout = layout)

        running = True
        while running:
            event, values = window.read()

            match event:
                case sg.WINDOW_CLOSED:
                    running = False
                    break

                case _:
                    break

        window.close()