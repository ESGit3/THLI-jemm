
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput



class TestApp(App):
    @staticmethod
    def build():
        return Button(text='Hello World')
###
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
    print("stuff)")

btimer = Button (text="Start", font_size=7)
btimer.bind(on_press=timer)




class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
###
TestApp().run()


# taskkill
def killProcess(taskName):
    os.system("taskkill /f /im " + taskName)

killProcess("/Applications/Discord.app")

# mongodb
cluster = MongoClient("mongodb+srv://jkska23:<teenhacksdb>@cluster0-ctd6l.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["teenhacks"]
collection = db[""]

def uinfo():
    q = input("Would you like to sign up?: (Y/N) \n")
    if q == "Y":
        uid = input("Enter your nickname: \n")
        umail = input("Enter your email: \n")
        upass = input("Enter your password: \n")
        post = {"_id": uid, "email": umail, "password": upass}
        user.insert_one(post)
        print("Your account has been made!")
    else:
        print("You can sign in with your gmail to submit your points")

def viewScore():
    print("work on it")


user.insert_one({"_id": bot1, "email": test1@gmail.com, "password": 12345, "score": 3})
user.insert_one({"_id": bot2, "email": test2@gmail.com, "password": 12345, "score": 2})
user.insert_one({"_id": bot3, "email": test3@gmail.com, "password": 12345, "score": 1})



def ucinfo(): #this is for chaning into that i can work on later
    q = input("Would you like to change your information?: (Y/N) \n")
    if q == "Y":
        print("something")
    else:
        print("You can always access this information and change your information")



#
# existQ = collection.find({"name": bill})
# for i in existQ:
#     print(i["_id"])  # gives the ID of the user with name bill

# # i just put this here to make it easier for me to pull
# # git pull https://github.com/ESGit3/THLI-jemm.git
