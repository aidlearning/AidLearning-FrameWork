from cvs import *

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=120, height=100)
        self.lbl = gui.Label('Hello world!')
        self.bt = gui.Button('Hello name!')
        self.bt2 = gui.Button('Hello name surname!')

        # setting the listener for the onclick event of the buttons
        self.bt.onclick.do(self.on_button_pressed, "Name")
        self.bt2.onclick.do(self.on_button_pressed, "Name", "Surname")

        # appending a widget to another
        container.append(self.lbl)
        container.append(self.bt)
        container.append(self.bt2)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget, name='', surname=''):
        self.lbl.set_text('Button pressed!')
        widget.set_text('Hello ' + name + ' ' + surname)

# starts the gui
initcv(cvs.openwin)
startcv(MyApp)