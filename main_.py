# necessario criar um arquivo .kv com mesmo nome do app ex. mytarefa.kv
# https://www.youtube.com/watch?v=-jM0BKWUKKk&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=6

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen):
    def __init__(self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def addWidget(self):
        texto=self.ids.texto.text
        if texto != "":
            self.ids.box.add_widget(Tarefa(text=texto))
            self.ids.texto.text = ""


class Tarefa(BoxLayout):
    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class MyTarefa(App):
    def build(self):
        return Gerenciador()

MyTarefa().run()

