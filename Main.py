import time

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


def viewScore():
    print("work on it")


def ucinfo(): #this is for changing info that i can work on later
    q = input("Would you like to change your information?: (Y/N) \n")
    if q == "Y":
        print("something")
    else:
        print("You can always access this information and change your information")

#####
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


def timer():
    print("stuff")

btimer = Button (text="Start", font_size=7)
btimer.bind(on_press=timer)



class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
######


# taskkill
def killProcess(taskName):
    os.system("taskkill /f /im " + taskName)

killProcess("/Applications/Discord.app")


#functions for buttons



# # i just put this here to make it easier for me to pull
# # git pull https://github.com/ESGit3/THLI-jemm.git




