# necessario criar um arquivo .kv com mesmo nome do app ex. mytarefa.kv
# https://www.youtube.com/watch?v=-jM0BKWUKKk&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=6


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size= 40, size_hint_y=None, heigth = 200 ))


class MyTarefa(App):
    def build(self):
        return Tarefas(['Compras Supermercado', "Pegar filha escola", "estudar especialização"])

MyTarefa().run()

