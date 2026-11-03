import FreeSimpleGUI as sg

class DataSourceManager:
    def show(self, app):
        source_layout = [
                                    [ sg.Text(text = "Dataset Name", key = "-DATASETNAME-") ],
                                    [ sg.Table(values = [["None"]], key = "-DATASOURCES-") ]
                                ]

        controls_layout = [
                                    [ sg.Button(button_text = "New Source", key = "-ADDSOURCE-") ],
                                    [ sg.Button(button_text = "Remove Source", key = "-REMOVESOURCE-") ],
                                    [ sg.Button(button_text = "Append Source", key = "-APPENDSOURCE-") ],
                                    [ sg.Button(button_text = "Remove Append", key = "-REMOVEAPPENDED-") ],
                                    [ sg.VPush() ],
                                    [ sg.Button(button_text = "Load Source", key = "-SELECT-") ]
                                  ]

        layout = [
                        [ sg.Table(values = [["None"]], key = "-DATASETS-"), sg.Column(source_layout), sg.Column(controls_layout) ]
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