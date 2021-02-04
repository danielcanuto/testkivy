from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class BateVolta(App):
    def build(self):
        # box = BoxLayout()
        box = BoxLayout(orientation='vertical')
        button = Button(text="Vamos de bate Volta")
        label = Label(text = "Testo 01")
        box.add_widget(button)
        box.add_widget(label)

        box2 = BoxLayout()
        button2 = Button(text="Vamos de bate Volta")
        label2 = Label(text = "Testo 02")
        box2.add_widget(button2)
        box2.add_widget(label2)

        box.add_widget(box2)
        
        
        return box


BateVolta().run()