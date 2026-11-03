import FreeSimpleGUI as sg

class DESWindow:
    def show(self, app):
        layout_column_1 = [
                                        [ sg.Graph(canvas_size = (100, 100), graph_bottom_left = (100, 100), graph_top_right = (0, 0), key = "-GRAPHDISPLAY-") ],
                                        [ sg.Graph(canvas_size = (100, 10), graph_bottom_left = (100, 10), graph_top_right = (0, 0), key = "-GRAPHCONTROLS-") ]
                                    ]

        layout_column_2 = [
                                        [ sg.Text(text = "Mode", key = "-APPMODE-"), sg.Button(button_text = "Configure", key = "-CONFIGURE-") ],
                                        [ sg.Multiline(disabled = True, key = "-DATASETDETAILS-") ],
                                        [ sg.Button(button_text = "Manage Data Sources", key = "-MANAGE-") ],
                                        [ sg.Multiline(disabled = True, key = "-GRAPHDESCRIPTION-") ]
                                    ]

        layout = [
                        [ sg.Column(layout = layout_column_1) ],
                        [ sg.Column(layout = layout_column_2) ]
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