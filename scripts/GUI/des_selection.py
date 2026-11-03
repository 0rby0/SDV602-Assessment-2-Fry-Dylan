import FreeSimpleGUI as sg

class DESSelection:
    def show(self, app):
        controls_layout = [
                                    [ sg.Button(button_text = "Sign Out") ],
                                    [ sg.Button(button_text = "Create") ],
                                    [ sg.Button(button_text = "Delete") ],
                                    [ sg.Button(button_text = "Select") ]
                                  ]

        search_layout = [
                        [ sg.Text("Username", key = "-USERNAME-"), sg.Input(key = "-SEARCH-") ],
                        [ sg.Table(values = [["None"]], key = "-SESSIONS-") ]
                    ]

        layout = [
                        [ sg.Column(search_layout), sg.Column(controls_layout) ]
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