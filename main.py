from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):

        btn = Button(text = "[b]This is button[/b]", markup=True, background_color=(.84,.32,.42,.5))
        txt = Label(text = "[color=#254686]This is Label[/color]", markup=True)
        btn.on_press = test
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)

        return layout

def test():
    print("Hello!")

app = MyApp()
app.run()