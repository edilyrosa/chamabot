from cgitb import text
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
text = "Hola mundo"
engine.say(text)
engine.runAndWait()