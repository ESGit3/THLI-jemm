# Sample Python application demonstrating the
# working of FloatLayout in Kivy

import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# module consist the floatlayout
# to work with FloatLayout first
# you have to import it
from kivy.uix.floatlayout import FloatLayout

# To change the kivy default settings
# we use this module config
from kivy.config import Config

from kivy.uix.textinput import TextInput

Config.set('graphics', 'resizable', True)


# creating the App class
class LoginScreenApp(App):

    def build(self):
        # creating Floatlayout
        Fl = FloatLayout()

        # creating button
        # a button 30 % of the width and 20 %
        # of the height of the layout and
        # positioned at (300, 200), you can do:
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

        # adding widget i.e button
        Fl.add_widget(btn)
        Fl.add_widget(btn2)
        Fl.add_widget(btn3)
        Fl.add_widget(btn4)

        # return the layout
        return Fl

    # run the App


if __name__ == "__main__":
    LoginScreenApp().run()

