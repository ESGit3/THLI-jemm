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


#####
class LoginScreenApp(App):

    # def submit(self, btn):
    #     self.add_widget(Label(text='info: ' + self.password.text))
    #
    # def __init__(self, **kwargs):
    #     super(LoginScreen, self).__init__(**kwargs)
    #     self.cols = 2
    #     self.add_widget(Label(text='User Name'))
    #     self.username = TextInput(multiline=False)
    #     userInput = self.add_widget(self.username)
    #     self.add_widget(Label(text='Password'))
    #     self.password = TextInput(text='', multiline=False)
    #     self.add_widget(self.password)
    #     submitBtn = Button(text="Submit")
    #     self.add_widget(submitBtn)
    #     submitBtn.bind(on_press=self.submit)

    def build(self):
        Fl = FloatLayout()
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        Fl.add_widget(btn1)
        self.lbl1 = Label(text='Username',
                          size_hint=(.2, .05),
                          pos=(300, 800))
        Fl.add_widget(self.lbl1)
        self.txt1 = TextInput(size_hint=(.8, .05),
                              pos=(700, 800),
                              text='',
                              multiline=False)
        Fl.add_widget(self.txt1)

    def buttonClicked(self, btn):
        self.lbl1.text = "You wrote " + self.txt1.text


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
        return LoginScreen()


if __name__ == '__main__':
    LoginScreenApp().run()


######


# taskkill
def killProcess(taskName):
    os.system("taskkill /f /im " + taskName)


killProcess("/Applications/Discord.app")

# functions for buttons


# # i just put this here to make it easier for me to pull
# # git pull https://github.com/ESGit3/THLI-jemm.git
