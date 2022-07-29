import pyttsx3

engine = pyttsx3.init()
say_some = input("Please write some thing in your command line: ")
engine.say(say_some)
engine.runAndWait()
