import FreeSimpleGUI as sg

class ChatWindow:
    def show(self):
        layout = [
                        [ sg.Text("Session Name", size = (40, 1), justification = "center", key = "-SESSIONNAME-") ],
                        [ sg.HorizontalSeparator() ],
                        [ sg.Multiline(size = (47, 25), disabled = True, key = "-CHATLOG-") ],
                        [ sg.Input(key = "-MESSAGEINPUT-"), sg.Button(">", key = "-SUBMIT-") ]
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