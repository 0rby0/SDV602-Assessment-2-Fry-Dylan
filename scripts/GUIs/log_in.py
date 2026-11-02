import FreeSimpleGUI as sg

class LogIn:
    def show(self):
        title = [[sg.Text("DES Analysis App")]]

        input = [
                        [sg.Text("Login")],
                        [sg.Text("Username"), sg.Input()],
                        [sg.Text("Password"), sg.Input()],
                        [sg.Button("Submit")],
                        [sg.Button("Don't have an account? Sign Up")]
                    ]

        layout = [
                        [sg.Column(title), sg.Column(input)]
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