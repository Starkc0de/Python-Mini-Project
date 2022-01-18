import speech_recognition as sr
import webbrowser
import datetime
import pyttsx3
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")

            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print(" Not Understand ")    

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    # if sptext().lower() == "hey peter":
        
        data1 = sptext().lower()

        if "your name" in data1:
            name = "my name is friday"
            speechtx(name)

        elif "old are you" in data1:    
            age = "i am 4 years old"
            speechtx(age)

        
    # else:
    #     print("thanks")    
