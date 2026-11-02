import FreeSimpleGUI as sg

class SessionCreator:
    def show(self):
        layout = [
                        [sg.Text("Create Session")],
                        [sg.Text("Session Name"), sg.Input()],
                        [sg.Button("Cancel"), sg.Checkbox("Public"), sg.Button("Create")]
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