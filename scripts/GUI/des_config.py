import FreeSimpleGUI as sg

class DESConfig:
    def show(self, app):
        layout = [
                        [ sg.Text("Type"), sg.Combo(values = ["Line", "Pie", "Bar"], key = "-TYPESELECT-") ],
                        [ sg.Text("Y Key"), sg.Combo(values = ["None"], key = "-YSELECT-") ],
                        [ sg.Text("X Key"), sg.Combo(values = ["None"], key = "-XSELECT-") ],
                        [ sg.Text("Legend"), sg.Combo(values = ["None"], key = "-LEGENDSELECT-") ],
                        [ sg.Text("Legend Series"), sg.Combo(values = ["None"], key = "-SUBLEGENDSELECT-") ],
                        [ sg.Button(button_text = "Cancel", key = "-CANCEL-"), sg.Button(button_text = "Submit", key = "-SUBMIT-") ]
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