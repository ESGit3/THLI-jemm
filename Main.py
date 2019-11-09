from pymongo import MongoClient

import pymongo
import time

#pomodoro


# timer
mins = 25

def timer():
    while mins != 0:
        print(">>>>>>>>>>>>>>>>>>>>>" + mins)
        time.sleep(60)
        mins -= 1



# taskkill
def killProcess(taskName):
    os.system("taskkill /f /im " + taskName)


killProcess("/Applications/Discord.app")


# mongodb
cluster = MongoClient("mongodb+srv://jkska23:<teenhacksdb>@cluster0-ctd6l.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["teenhacks"]
collection = db[""]

# study, example
post = {"_id": 1, "user": user1, "password": 12345, "score": 0}  # make it the same structure as dictionaries
users.insert_one(post)

existQ = collection.find({"name": bill})
for i in existQ:
    print(i["_id"])  # gives the ID of the user with name bill

# i just put this here to make it easier for me to pull
# git pull https://github.com/ESGit3/THLI-jemm.git
