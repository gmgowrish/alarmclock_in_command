import datetime
from pygame import mixer

import pyttsx3

engine = pyttsx3.init()
alarmH = int(input("Enter Hour:"))
alarmM = int(input("Enter Minutes:"))
alarmS = int(input("enter the second"))
alarmAM = input("am/ pm:")

if alarmAM == "pm":
    alarmH += 12


def sound_alarm():
    mixer.init()
    mixer.music.load('the-score-revolution.ogg')
    mixer.music.play()


while True:
    if alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute and alarmS == datetime.datetime.now().second:
        print("playing... press ctrl + f2 to stop alarm")
        sound_alarm()

        text = "wakeup Gowrish, What you do today can improve all your tomorrows."
        engine.setProperty("rate", 100)
        engine.say(text)
        engine.runAndWait()






