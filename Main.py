import os

def killProcess(name):
    os.system("taskkill /f /im " + name)


killProcess("Discord.app")