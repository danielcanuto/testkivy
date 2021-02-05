from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Incrementador(BoxLayout):
    pass


class BateVolta(App):
    def build(self):
        return Incrementador()

BateVolta().run()

