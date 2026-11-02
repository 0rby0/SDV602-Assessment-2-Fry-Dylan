import FreeSimpleGUI as sg

class DESWindow:
    def show(self):
        layout_column_1 = [
                                        [sg.Graph(canvas_size = (100, 100), graph_bottom_left = (100, 100), graph_top_right = (0, 0))],
                                        [sg.Graph(canvas_size = (100, 10), graph_bottom_left = (100, 10), graph_top_right = (0, 0))]
                                    ]

        layout_column_2 = [
                                        [sg.Text("Mode"), sg.Button("Configure")],
                                        [sg.Multiline(disabled = True)],
                                        [sg.Button("Manage Data Source")],
                                        [sg.Multiline(disabled = True)]
                                    ]

        layout = [
                        [sg.Column(layout = layout_column_1)],
                        [sg.Column(layout = layout_column_2)]
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