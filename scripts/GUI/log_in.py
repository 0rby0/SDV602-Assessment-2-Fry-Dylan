import FreeSimpleGUI as sg

class LogIn:
    def show(self):
        title = [ [sg.Text("DES Analysis App")] ]

        input_layout = [
                        [ sg.Text("Login") ],
                        [ sg.Text("Username"), sg.Input(key = "-USERNAME-") ],
                        [ sg.Text("Password"), sg.Input(key = "-PASSWORD-") ],
                        [ sg.Button(button_text = "Submit", key = "-SUBMIT-") ],
                        [ sg.Button("Don't have an account? Sign Up", key = "-SIGNUP-") ]
                    ]

        layout = [
                        [ sg.Column(title), sg.Column(input_layout) ]
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