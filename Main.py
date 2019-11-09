from kivy.app import App
from kivy.uix.button import Button

uscores = 0 #this will be the total points assigned per 25min and reset when user quits the program completely

class TestApp(App):
    @staticmethod
    def build():
        return Button(text='Hello World')

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
    else:
        print("You can sign in with your gmail to submit your points")







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
