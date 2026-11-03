import FreeSimpleGUI as sg

class SignUp:
    def show(self, app):
        title = [[ sg.Text("DES Analysis App") ]]

        input_layout = [
                        [ sg.Text("Sign Up") ],
                        [ sg.Text("Username"), sg.Input(key = "-USERNAME-") ],
                        [ sg.Text("Password"), sg.Input(key = "-PASSWORD-") ],
                        [ sg.Button(button_text = "Submit", key = "-SUBMIT-") ],
                        [ sg.Button(button_text = "Already have an account? Log In", key = "-LOGIN-") ]
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