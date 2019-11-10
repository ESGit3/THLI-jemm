import time
import json

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics', 'resizable', True)


def viewScore():
    print("work on it")


def ucinfo():  # this is for changing info that i can work on later
    q = input("Would you like to change your information?: (Y/N) \n")
    if q == "Y":
        print("something")
    else:
        print("You can always access this information and change your information")


class LoginScreenApp(App):
    def build(self):
        Fl = FloatLayout()
        lbl1 = Label(text='Username',
                     size_hint=(.2, .05),
                     pos=(300, 800))
        txt1 = TextInput(size_hint=(.8, .05),
                         pos=(700, 800),
                         text='',
                         multiline=False)
        lbl2 = Label(text='')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)

        Fl.add_widget(btn1)
        Fl.add_widget(lbl1)
        Fl.add_widget(txt1)
        Fl.add_widget(lbl2)
        return Fl

    def buttonClicked(self):
        lbl2.text = "You wrote " + txt1.text


# def timer():
#    t = 1500 #25min * 60 secs
#    while t > 0:
#        print(str(t // 60) + " : " + str(1500 % 60))
#        t -= 1
#        if t == 0:
#            uname = input("Enter your username to add a point: \n")


# btimer = Button (text="Start", font_size=7)
# btimer.bind(on_press=timer)


class MyApp(App):

    def build(self):
        return LoginScreenApp()


if __name__ == '__main__':
    LoginScreenApp().run()


######


# taskkill
class MyGrid(GridLayout):
    def __init__(self, **kwarqs):
        super(MyGrid, self), __init__(**kwarqs)
        self.cols = 1

        self.inside = GridLayout
        self.inside.cols = 2

        self.cols = 2
        self.inside.add_widget(Label (text="Input the name of the program you want to kill"))
        self.CP = TextInput(Multiline=False)
        self.inside.add_widget(self.CP)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit")
        self.add_widget(self.submit)

class MyApp(App):
    def build(self):
        return MyGrid()

def killProcess(taskName):
    while True:
        os.system("taskkill /IM " + taskName + " /F")

#killProcess("/Applications/Discord.app")




# # i just put this here to make it easier for me to pull
# # git pull https://github.com/ESGit3/THLI-jemm.git
