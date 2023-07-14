import pyaudio
from covid import Covid #pip install covid
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Artificial Intellegence: " +audio)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def covid():
    speak("which country sir")
    case= takeCommand().lower()
    #covid=Covid(source="worldometers")
    covid=Covid()
    cases=covid.get_status_by_country_name(str(case))
    for x in cases:
        print(x,":",cases[x])


if __name__ == "__main__":
        while True:
        query = takeCommand().lower()

        if 'covid news' in query or "coronavirus" in query:
            covid()
