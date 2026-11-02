import FreeSimpleGUI as sg

class DESSelection:
    def show(self):
        controls_layout = [
                                    [sg.Button("Sign Out")],
                                    [sg.Button("Create")],
                                    [sg.Button("Delete")],
                                    [sg.Button("Select")]
                                  ]

        search_layout = [
                        [sg.Text("Username"), sg.Text()],
                        [sg.Table([["None"]])]
                    ]

        layout = [
                        [sg.Column(search_layout), sg.Column(controls_layout)]
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