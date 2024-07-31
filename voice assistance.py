import pyttsx3
import wikipedia
voice=pyttsx3.init()
text=input("Searching wikipedia/Google:")
result=wikipedia.summary(text,sentences=4)
print(result)
voice.say(result)
voice.runAndWait()
