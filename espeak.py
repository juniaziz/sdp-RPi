import pyttsx
engine = pyttsx.init()
text = 'warning! Red light ahead'
engine.say(text)
engine.runAndWait()
