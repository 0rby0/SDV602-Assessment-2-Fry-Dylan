import FreeSimpleGUI as sg

class DESConfig:
    def show(self):
        layout = [
                        [sg.Text("Type"), sg.Combo(["Line", "Pie", "Bar"])],
                        [sg.Text("Y Key"), sg.Combo(["None"])],
                        [sg.Text("X Key"), sg.Combo(["None"])],
                        [sg.Text("Legend"), sg.Combo(["None"])],
                        [sg.Text("Legend Series"), sg.Combo(["None"])],
                        [sg.Button("Cancel"), sg.Button("Submit")]
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