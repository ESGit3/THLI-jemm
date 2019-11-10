import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.textinput import TextInput

Config.set('graphics', 'resizable', True)


class LoginScreenApp(App):

    def build(self):
        Fl = FloatLayout()
        btn = Button(text='Username',
                     size_hint=(.2, .05),
                     pos=(300, 800))
        btn2 = Button(text='Password',
                     size_hint=(.2, .05),
                     pos=(300, 500))
        btn3 = TextInput(size_hint=(.8, .05),
                      pos=(700, 800))
        btn4 = TextInput(size_hint=(.8, .05),
                      pos=(700, 500))


        Fl.add_widget(btn)
        Fl.add_widget(btn2)
        Fl.add_widget(btn3)
        Fl.add_widget(btn4)


        return Fl

