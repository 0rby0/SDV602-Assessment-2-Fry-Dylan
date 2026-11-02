import FreeSimpleGUI as sg

class ChatWindow:
    def show(self):
        layout = [
                        [sg.Text("Session Name", size = (40, 1), justification = "center")],
                        [sg.HorizontalSeparator()],
                        [sg.Multiline(size = (47, 25), disabled = True)],
                        [sg.Input(), sg.Button(">")]
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