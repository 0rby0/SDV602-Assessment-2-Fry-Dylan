import FreeSimpleGUI as sg

class DataSourceManager:
    def show(self):
        source_layout = [
                                    [sg.Text("Source 1")],
                                    [sg.Table([["None"]])]
                                ]

        controls_layout = [
                                    [sg.Button("New Source")],
                                    [sg.Button("Remove Source")],
                                    [sg.Button("Append Source")],
                                    [sg.Button("Remove Append")],
                                    [sg.VPush()],
                                    [sg.Button("Load Source")]
                                  ]

        layout = [
                        [sg.Table([["None"]]), sg.Column(source_layout), sg.Column(controls_layout)]
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