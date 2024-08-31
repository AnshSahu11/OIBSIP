import pyttsx3 as p
import speech_recognition as sr
import datetime
import webbrowser

#initialize
engine = p.init()
r= sr.Recognizer()
rate = engine.getProperty("rate")
engine.setProperty('rate',200)
voice= engine.getProperty('voices')
engine.setProperty("voices",voice[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
#loop
while True:
    try:
      with sr.Microphone() as source:
          print('Listening..')
          audio = r.listen(source, timeout =10)
          text=r.recognize_google(audio)
          print(text)
        
          print("You said:", text)

          if "hello" in text.lower():
                speak("hello sir i'm your voice assistant. how are you")
          elif "what about you" in text.lower():
                speak("i am having a good day sir")
                speak("what can i do for you??")
          elif "what is your name" in text.lower():
                speak("My name is nova")
          elif "date" in text.lower():
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                speak("Today's date is " + current_date)
          elif "time" in text.lower():
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak("It's " + current_time)
          elif "play music" in text.lower():
                speak("opening spotify.")
                webbrowser.open("open.spotify.com")
          elif 'open google' in text.lower():
                webbrowser.open("google.com")
          elif 'open calculator' in text.lower():
                webbrowser.open("calculator.net")
          elif 'open instagram' in text.lower():
                webbrowser.open("instagram.com")
          elif 'weather' in text.lower():
                webbrowser.open("accuweather.com")
          elif "goodbye" or "good bye" in text():
                speak("Goodbye!") 
                break 
          else:
                speak("Sorry, I didn't understand that.")
                break

    except sr.UnknownValueError:
        print("Could not understand audio")