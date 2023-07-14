from __future__ import print_function
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from googletrans import Translator #pip install googletrans
import binascii
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import wikipedia #pip install wikipedia
from email.mime.text import MIMEText
from email.parser import Parser
import webbrowser
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import mimetypes
import time
import pyautogui
import subprocess
import errno
import codecs
import sys
import mimetypes
from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from optparse import OptionParser
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyjokes #pip install pyjokes
import PIL.Image, PIL.ImageTk    #pip install pillow
from twilio.rest import Client #pip install twilio
from twilio.twiml.messaging_response import MessagingResponse #pip install twilio
from flask import Flask,request,redirect #pip install flask
from email.message import EmailMessage
import wolframalpha #pip install wolframalpha
import os
import smtplib
import playsound #pip install playsound
import smtplib
import datetime #pip install datetime
from covid import Covid #pip install covid
import pickle
import psutil #pip install psutil
import wmi #pip install wmi
import os.path
import subprocess
import testcode #pip install testcode
from tkinter import *
from tkinter import scrolledtext
import random
from tkinter.ttk import *
from googletrans import Translator #pip install googletrans
import youtube_dl #pip install youtube_dl
import tkinter as tk
import roman #pip install roman
import pyowm #pip install pyowm
import sounddevice as sd #pip install sounddevice
import pyautogui #pip install pyautogui
import pyperclip #pip install pyperclip
import json
import requests
import instaloader #pip install instaloader
from urllib.request import urlopen
import time

INFO = '''
	        *=======================================*
	        |....JARVIS ARTIFICIAL INTELLIGENCE.....|
	        +---------------------------------------+
	        |#Name: J-A-R-V-I-S            	        |
	        |#Owner: Mohamed saqib                  |
	        |#Date: 01/08/2020                      |
	        *=======================================*
	        '''
print(INFO)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

wolframalpha_app_id = 'Q5K7GK-4ALY68KL5V'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Artificial Intellegence: " +audio)

#First of all you need to download rainmeter for this



name="Mohamed saqib"
age="15"
email_id="saqibjaveed2006@gmail.com"
email_id_password="j@veed77"
gender="Sir"
city="Al Rahba"
dad="+971504613543"
mom="0504613543"
sis="your-contacts-gmail"
account_sid = 'AC514f742479a47f6e6c1edf314d0c9e87'
auth_token = '6b6d7f61efa0c5eb381bafeb84b967c3'

client = Client(account_sid,auth_token)

startmin = int(datetime.datetime.now().hour)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Starting Engine")
    speak("Collecting required resources")
    speak("initializing")
    speak("Getting information from the CPU")
    speak("contacting with mail services")
    speak("importing preferences from home interface.")
    speak("system is now fully operational")
    playsound.playsound('power up.mp3')
    rainmeterPath=("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
    os.startfile(rainmeterPath)
    speak("I am Your Friend. developed by Mohamed Saqib")   
    speak("from Sunrise English Private School ")
    speak("class 9th A") 
    speak("principle Doctor Mister thakur mulchandani")  

def langtranslator():
    try:
        trans=Translator()
    

        speak("Say the language to translate in")
        language=takeCommand().replace(" ","")
            

        
        speak("what to translate")
        content=takeCommand()
            
        t=trans.translate(text=content,dest=language)
        speak(f"{t.origin} in {t.dest} is{t.text}")

    except:
        speak("error")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    speak("percent")

def battery():
    battery = psutil.sensors_battery()
    speak("the battery is at")
    speak(battery.percent )
    speak("percent")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saqibjaveed2006@gmail.com', 'j@veed77')
    server.sendmail('saqibjaveed2006@gmail.com', to, content)
    server.close()

def date():
    year= int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("date is")
    speak(date)
    speak("month is")
    speak(month)
    speak("years")
    speak(year)

def database():
    Exception 
    if "what do I have" in query:
        takeCommand()
    client = wolframalpha.Client('Q5K7GK-4ALY68KL5V')
    speak(f"Searching for {query} in my database")
    try:
        res = client.query(query)
        results = next(res.results).query
        speak(results)
    except:
        speak(f"Sir, your query {query} does not match any of the datani my data base.")
        speak("Try asking other things..")
        speak("sorry for in convinience sir")

def password():

    speak("Bismilllahh          hirr          Rahmaaannn          nirrr         Raaheem.......")
    speak("voice activation required to continue")
    e_passcode = takeCommand().lower()
    v_passcode = "cat"
    if e_passcode == v_passcode:
        speak("Welcome back sir")
    else:
        speak("access denied. Please try again later")
        quit()
        pyautogui.hotkey('alt','f4')

def covid():
    speak("which country sir")
    case= takeCommand().lower()
    #covid=Covid(source="worldometers")
    covid=Covid()
    cases=covid.get_status_by_country_name(str(case))
    for x in cases:
        print(x,":",cases[x])


def note(query):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(query)

    subprocess.Popen(["notepad.exe", file_name])

def jokes():
    speak(pyjokes.get_joke())

def twilio_call():

    global contacts 
    
    account_sid = 'AC514f742479a47f6e6c1edf314d0c9e87'
    auth_token = '6b6d7f61efa0c5eb381bafeb84b967c3'

    client = Client(account_sid,auth_token)

    contact_name=query.split("call")
    contact=contact_name[1]
    if "dad" in contact or "Dad"  in contact:
        to="+971504613543"

    if "mother" in contact  or "Mother" in contact in contact:
        to ="+971507923584"

    if "sister" in contact or "Sister" in contact:
        to="phone_number"

    else:
        speak(f"Hmmm seems like you have not registered the contact in my data base sir so, I cant call {contact}")
    
    try:
        speak(f"Trying to call {contact} on {to}")
        call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                            to=to,
                            from_='+12055092336'
                        )
    except:
        print("Error")

def recsound():
    fs=44100
    speak("what should be the length of your sound wave Plz answer in seconds")
    ans=int(takeCommand())
    seconds=ans

    recorded=sd.rec(int(seconds*fs),samplerate=fs,channels=2)
    sd.wait()
    speak("sucessfully recoreded")
    speak("what should i keep the file name")
    filename=takeCommand()
    type(filename+'.mp3',fs,recorded)
    speak("sucessfuly saved")
    try:
        speak("should i show you")
        reply=takeCommand()
        if "yes" in reply:
            os.startfile(filename+".mp3")

    except:
        if "no" in reply:
            speak("okay next command sir")


def repeatmyspeech():
    speak("Okay starting to listen")
    speak(f"{name} {gender} start speaking")
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-in')
        speak(f"{name} {gender} said: {said}\n")
        print(f"{name} {gender} hre is ur repetition by me {said}\n")
        try:
            speak("should i save the file?")
            ans=takeCommand()
            if "yes" in ans:
                try:
                    speak("What should i keep the file name")
                    filename=takeCommand().lower
                    said.save(filename+".mp3")   
                    speak("File saved sucessfully")
                    try:
                        speak("Do you want me to show it?")
                        reply=takeCommand()
                        if "yes" in reply:
                            os.startfile(filename+".mp3")
                            speak("here it is")

                    except: 
                            if "no" in reply:
                                speak("Never mind")

                except: 
                    speak("Error in keeping filename")

        except: 
                speak("Okay")

    except:
            return "None"
    return said


def Screenshot():
    image=pyautogui.screenshot()
    speak("screen shot taken")
    speak("what do you want to save it as?")
    filename=takeCommand()
    image.save(filename+".png")
    speak("do you want me to show it")
    ans=takeCommand()
    if "yes" in ans:
        os.startfile(filename+".png")
    else:
        speak("never mind")

def sign_in(meetingid,password):
    mid=meetingid
    pswd=password
    
    subprocess.call("C:\\Users\\Toshiba\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    
    time.sleep(2)
    
    join_btn1=pyautogui.locateCenterOnScreen(r'C:\\Users\\Toshiba\\OneDrive\\Documents\\jarvis-for-school-main\\join.PNG')
    pyautogui.moveTo(join_btn1)
    pyautogui.click(join_btn1)
    time.sleep(2)

    pyautogui.write(mid)
    
    join_btn2=pyautogui.locateCenterOnScreen(r'C:\\Users\\Toshiba\\OneDrive\\Documents\\jarvis-for-school-main\\join2.PNG')
    pyautogui.moveTo(join_btn2)
    pyautogui.click(join_btn2)
    time.sleep(2)
    
    pyautogui.write(pswd)
    
    join_btn3=pyautogui.locateCenterOnScreen(r'C:\\Users\\Toshiba\\OneDrive\\Documents\\jarvis-for-school-main\\join3.PNG')
    pyautogui.moveTo(join_btn3)
    pyautogui.click(join_btn3)
    


def read():
    pyautogui.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    speak(tobespoken)

def locate():
    place=query[1]
    speak(f"according to my data base {place} lies here")
    webbrowser.open_new_tab("https://www.google.com/maps/place/"+place)


pg = "pyautogui"

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

if __name__ == "__main__":
    # password()
    #wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query or "who is" in query or "what is" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif "repeat my speech" in query:
            repeatmyspeech()
        
        elif "record my sound" in query:
            recsound()
            
        elif "my current location" in query:
            locate()

        elif "read for me" in query or "read this" in query:
            read()


        elif "call" in query:
            twilio_call()

        elif "open zoom" in query or "zoom" in query:
            speak("accesing zoom server's")
            speak("starting zoom")
            ZoomPath=("C:\\Users\\Toshiba\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            os.startfile(ZoomPath)

        elif "close video call" in query or "close zoom" in query:
            speak("sir do you want to close zoom")
            reply = takeCommand()
            if "yes" in reply:
                speak("sir i am closing zoom")
                ZoomPath=("C:\\Users\\Toshiba\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
                os.system("TASKKILL /f /IM zoom.exe")

        elif "tempreture" in query:
            res = app.query(query)
            speak(next(res.results).text)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('the answer is : '+answer)
            speak('the answer is : '+answer)

        elif "open note pad" in query:
            note(query)

        elif "database" in query:
            database()
            
        elif "documents" in query:
            subprocess.run("explorer ::{20D04FEQ-3AEA-1069-A2D8-080028303090}")

        elif "desktop" in query:
            subprocess.run("explorer %sernam%")

        elif 'covid news' in query or "coronavirus" in query:
            covid()

        elif "battery status" in query:
            battery()

        elif "cpu status" in query:
            cpu()

        elif "write down something" in query or "set a reminder" in query:
            speak("what to you want to write down")
            note = takeCommand()
            remember = open("data.txt", 'w')
            remember.write(note)
            remember.close()
            speak("i have noted the remainder" + note)

        elif "do you have anything to remember" in query or "any reminder today" in query:
            remember = open("data.txt", "r").read()
            speak("you told me to remember that" + remember)

        elif "origin" in query or "originate" in query:
            print("Coronavirus disease 2019 (COVID-19) is defined as illness caused by a novel coronavirus now called severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2; formerly called 2019-nCoV),") 
            print("which was first identified amid an outbreak of respiratory illness cases in Wuhan City, Hubei Province, China.")
            print("It was initially reported to the World Health Organization  on December 31, 2019. On January 30, 2020, the World Health Organization  declared the COVID-19 outbreak a global health emergency.")
            print("On March 11, 2020, the World Health Organization  declared COVID-19 a global pandemic, its first such designation since declaring H1N1 influenza a pandemic in 2009")
            speak("Coronavirus disease 2019 (COVID-19) is defined as illness caused by a novel coronavirus now called severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2; formerly called 2019-nCoV),") 
            speak("which was first identified amid an outbreak of respiratory illness cases in Wuhan City, Hubei Province, China.")
            speak("It was initially reported to the World Health Organization  on December 31, 2019. On January 30, 2020, the World Health Organization  declared the COVID-19 outbreak a global health emergency.")
            speak("On March 11, 2020, the World Health Organization  declared COVID-19 a global pandemic, its first such designation since declaring H1N1 influenza a pandemic in 2009")

        elif "vaccine update" in query:
            print("NEW YORK (Reuters) - Drugmakers and research centers around the world are working on COVID-19 vaccines,") 
            print("with large global trials of several of the candidates involving tens of thousands of participants well underway.")
            speak("NEW YORK (Reuters) - Drugmakers and research centers around the world are working on COVID-19 vaccines,") 
            speak("with large global trials of several of the candidates involving tens of thousands of participants well underway.")

        elif "vaccine" in query:
            print("Not yet. Many potential vaccines for COVID-19 are being studied, and several large clinical trials may report results later this year.")
            print("If a vaccine is proven safe and effective, it must be approved by national regulators, manufactured to exacting standards, and distributed. World Health Organization is working with partners around the world to help coordinate key steps in this process.") 
            print("Once a safe and effective vaccine is available, World Health Organization will work to facilitate equitable access for the billions of people who will need it")
            speak("Not yet. Many potential vaccines for COVID-19 are being studied, and several large clinical trials may report results later this year.")
            speak("If a vaccine is proven safe and effective, it must be approved by national regulators, manufactured to exacting standards, and distributed. World Health Organization is working with partners around the world to help coordinate key steps in this process.") 
            speak("Once a safe and effective vaccine is available, World Health Organization will work to facilitate equitable access for the billions of people who will need it")

        elif "vaccine stop the pandemic" in query:
            print("The impact of COVID-19 vaccines on the pandemic will depend on several factors.  These include factors such as the effectiveness of the vaccines; how quickly they are approved, manufactured, and delivered; and how many people get vaccinated.")
            print("Most scientists anticipate that, like most other vaccines, COVID-19 vaccines will not be 100 percent effective.")
            print("World Health Organization is working to help ensure that any approved vaccines are as effective as possible, so they can have the greatest impact on the pandemic.")
            speak("The impact of COVID-19 vaccines on the pandemic will depend on several factors.  These include factors such as the effectiveness of the vaccines; how quickly they are approved, manufactured, and delivered; and how many people get vaccinated.")
            speak("Most scientists anticipate that, like most other vaccines, COVID-19 vaccines will not be 100 percent effective.")
            speak("World Health Organization is working to help ensure that any approved vaccines are as effective as possible, so they can have the greatest impact on the pandemic.")

        elif "precautions" in query or "spread" in query or "spreads" in query:
            print("Washing hands with soap and water or using alcohol-based hand rub kills viruses that may be on your hands.")
            print("Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing.")
            print("Covering mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately.")
            print("Avoid touching your eyes, nose or mouth without washing your hands.")
            print("Avoid shaking hands and just wave.") 
            print("Avoid nose-to-nose greeting, hugging or kissing others.")
            print("Avoid contact with animals (live or dead).")
            print("Take enough rest and take a large amount of fluids.")
            speak("Washing hands with soap and water or using alcohol-based hand rub kills viruses that may be on your hands.")
            speak("Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing.")
            speak("Covering mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately.")
            speak("Avoid touching your eyes, nose or mouth without washing your hands.")
            speak("Avoid shaking hands and just wave.") 
            speak("Avoid nose-to-nose greeting, hugging or kissing others.")
            speak("Avoid contact with animals (live or dead).")
            speak("Take enough rest and take a large amount of fluids.")

        elif "transmitted by food" in query or "spread through food" in query:
            print("There is currently no evidence that people can catch COVID-19 from food.") 
            print("The virus that causes COVID-19 can be killed at temperatures similar to that of other known viruses and bacteria found in food")
            speak("There is currently no evidence that people can catch COVID-19 from food.") 
            speak("The virus that causes COVID-19 can be killed at temperatures similar to that of other known viruses and bacteria found in food")

        elif "spread by raw food" in query or "covid spread through raw food" in query:
            print("As a general rule, the consumption of raw or undercooked animal products should be avoided.")
            print("Raw meat, raw milk or raw animal organs should be handled with care to avoid cross- contamination with uncooked foods")
            speak("As a general rule, the consumption of raw or undercooked animal products should be avoided.")
            speak("Raw meat, raw milk or raw animal organs should be handled with care to avoid cross- contamination with uncooked foods")

        elif "food should be avoided" in query or "food to avoid during covid-19" in query:
            print("When cooking and preparing food, limit the amount of salt and high-sodium condiments (example soy sauce and fish sauce).")
            print("Limit your daily salt intake to less than 5 g (approximately 1 teaspoon), and use iodized salt.")
            print("Avoid foods (example snacks) that are high in salt and sugar.")
            print("Limit your intake of soft drinks or sodas and other drinks that are high in sugar (examples. fruit juices, fruit juice concentrates and syrups, flavoured milks and yogurt drinks)")
            print("Choose fresh fruits instead of sweet snacks such as cookies, cakes and chocolate.")
            speak("When cooking and preparing food, limit the amount of salt and high-sodium condiments (example soy sauce and fish sauce).")
            speak("Limit your daily salt intake to less than 5 g (approximately 1 teaspoon), and use iodized salt.")
            speak("Avoid foods (example snacks) that are high in salt and sugar.")
            speak("Limit your intake of soft drinks or sodas and other drinks that are high in sugar (examples. fruit juices, fruit juice concentrates and syrups, flavoured milks and yogurt drinks)")
            speak("Choose fresh fruits instead of sweet snacks such as cookies, cakes and chocolate.")

        elif "patient quarantin in hospitals" in query:
            print("World Health Organization advises that all confirmed cases, even mild cases, should be isolated in health facilities, to prevent transmission and provide adequate care.")
            print("But we recognize that many countries have already exceeded their capacity to care for mild cases in dedicated health facilities.")
            print("In that situation, countries should prioritize older patients and those with underlying conditions.") 
            speak("World Health Organization advises that all confirmed cases, even mild cases, should be isolated in health facilities, to prevent transmission and provide adequate care.")
            speak("But we recognize that many countries have already exceeded their capacity to care for mild cases in dedicated health facilities.")
            speak("In that situation, countries should prioritize older patients and those with underlying conditions.")

        elif "types of corona" in query:
            print("Six species of human coronaviruses are known, with one species subdivided into two different strains, making seven strains of human coronaviruses altogether.")
            speak("Six species of human coronaviruses are known, with one species subdivided into two different strains, making seven strains of human coronaviruses altogether.")
            speak("sir do you want to know the types of coronavirus")
            reply = takeCommand().lower()
            if "yes" in reply:
                print("Coronaviruses are a large family of viruses that are known to cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS).")
                speak("Coronaviruses are a large family of viruses that are known to cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS).")

        elif "age all group affected" in query or "are all age group affected" in query or "affected" in query:
            print("The COVID-19 virus infects people of all ages. However, evidence to date suggests that two groups of people are at a higher risk of getting severe COVID-19 disease.") 
            print("These are older people; and those with underlying medical conditions")
            speak("The COVID-19 virus infects people of all ages. However, evidence to date suggests that two groups of people are at a higher risk of getting severe COVID-19 disease.") 
            speak("These are older people; and those with underlying medical conditions")

        elif "sewage" in query:
            print("There is no evidence that the COVID-19 virus has been transmitted via sewerage systems with or without wastewater treatment")
            speak("There is no evidence that the COVID-19 virus has been transmitted via sewerage systems with or without wastewater treatment")

        elif "smokers at higher risk" in query or "smokers" in query or "smoker" in query or "smoking" in query:
            print("A review of studies by public health experts convened by WHO on 29 April 2020 found that smokers are more likely to develop severe disease with COVID-19, compared to non-smokers.")
            print("COVID-19 is an infectious disease that primarily attacks the lungs. Smoking impairs lung function making it harder for the body to fight off coronaviruses and other diseases")
            speak("A review of studies by public health experts convened by WHO on 29 April 2020 found that smokers are more likely to develop severe disease with COVID-19, compared to non-smokers.")
            speak("COVID-19 is an infectious disease that primarily attacks the lungs. Smoking impairs lung function making it harder for the body to fight off coronaviruses and other diseases")

        elif "heat" in query:
            print(" Exposing yourself to the sun or temperatures higher than 25°C DOES NOT protect you from COVID-19. You can catch COVID-19, no matter how sunny or hot the weather is.")
            print("Countries with hot weather have reported cases of COVID-19.")
            speak("Exposing yourself to the sun or temperatures higher than 25°C DOES NOT protect you from COVID-19. You can catch COVID-19, no matter how sunny or hot the weather is.")
            speak("Countries with hot weather have reported cases of COVID-19.")

        #elif "mask is recommended" in query or "mask":
            print("Fabric masks are recommended to prevent onward transmission in the general population in public areas")
            speak("Fabric masks are recommended to prevent onward transmission in the general population in public areas")

        elif "blood donation" in query:
            print("Blood Donation is safe for Healthy People")
            print("as the ministry of health and ptevention")
            print("along with health authorities implement")
            print("standard sterilizationand disinfection")
            print("procedure to prevent the transmission of infections")
            speak("Blood Donation is safe for Healthy People")
            speak("as the ministry of health and ptevention")
            speak("along with health authorities implement")
            speak("standard sterilizationand disinfection")
            speak("procedure to prevent the transmission of infections")

        elif "source of covid-19" in query:
            print("The source of Coronavirus 2019 (COVID-19) has not yet been identified. Early on in the outbreak, many of the patients in Wuhan, China, reportedly had some link to a large seafood and animal market, suggesting the likelihood that the virus emerged from an animal source. Analysis of the genetics of this virus is ongoing, to ascertain the exact source of the virus.")
            speak("The source of Coronavirus 2019 (COVID-19) has not yet been identified. Early on in the outbreak, many of the patients in Wuhan, China, reportedly had some link to a large seafood and animal market, suggesting the likelihood that the virus emerged from an animal source.")
            speak("Analysis of the genetics of this virus is ongoing, to ascertain the exact source of the virus.")

        elif "symptoms" in query:
            print("If you have mild symptoms and no history of travel in the last 14 days, we advise you to stay home and treat your symptoms as you would an ordinary cold or flu.")
            print("If you returned from abroad within the last 14 days and are now experiencing symptoms, you should visit your nearest primary health care center for a medical assessment.")
            speak("If you have mild symptoms and no history of travel in the last 14 days, we advise you to stay home and treat your symptoms as you would an ordinary cold or flu.")
            speak("If you returned from abroad within the last 14 days and are now experiencing symptoms, you should visit your nearest primary health care center for a medical assessment.")

        elif "isolation" in query:
            print("Isolation is the separation of those who are infected, or those suspected of being infected, from those who are healthy and it lasts for the duration of the disease infection.")
            speak("Isolation is the separation of those who are infected, or those suspected of being infected, from those who are healthy and it lasts for the duration of the disease infection.")

        elif  "quarantine" in query or "quarantin meaning" in query:
            print("Quarantines restricts the activities of healthy people for a period of time as determined by competent medical authorities.")
            speak("Quarantines restricts the activities of healthy people for a period of time as determined by competent medical authorities.")

        elif "tested for covid-19" in query or "test" in query:
            print("Anyone who has travelled abroad recently and then develops respiratory symptoms like fever, cough, or breathing difficulty, will be advised to visit their nearest primary health care center for medical assessment and diagnosis.")
            speak("Anyone who has travelled abroad recently and then develops respiratory symptoms like fever, cough, or breathing difficulty, will be advised to visit their nearest primary health care center for medical assessment and diagnosis.")

        elif "incubation period" in query or "incubation" in query:
            print("The term “incubation period” means the time between catching the virus and the time when symptoms first show.")
            print(" Most estimates of the incubation period for COVID-19 range from 2-14 days.")
            speak("The term “incubation period” means the time between catching the virus and the time when symptoms first show.")
            speak(" Most estimates of the incubation period for COVID-19 range from 2-14 days.")

        elif "what is the treatment" in query or "treatment" in query:
            print("There is currently no specific antiviral treatment recommended for COVID-19 infection. People infected with COVID-19 should receive supportive care to help relieve symptoms.")
            speak("There is currently no specific antiviral treatment recommended for COVID-19 infection. People infected with COVID-19 should receive supportive care to help relieve symptoms.")


        elif 'search in chrome'  in query:
            speak("what should i search sir")
            search = takeCommand()
            chromePath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chromePath).open_new_tab(search+'.com')

        elif "open edge" in query:
            edgePath=("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            os.startfile(edgePath)

        elif "open explorer" in query:
            explorerPath=("C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe")
            os.startfile(explorerPath)

        elif "open powerpoint" in query or "open ppt" in query:
            explorerPath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            os.startfile(explorerPath)

        elif "open Esheets" in query or "open Excel" in query:
            ExelPath=("C:\\Program Files\\Microsoft Office\\root\Office16\\EXCEL.EXE")
            os.startfile(ExelPath)

        elif "open word" in query or "open Word" in query:
            ExelPath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            os.startfile(ExelPath)

        elif "open outlook" in query or "open Outlook" in query:
            ExelPath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
            os.startfile(ExelPath)

        elif "open Publisher" in query or "open publisher" in query:
            ExelPath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE")
            os.startfile(ExelPath)

        elif "open skype" in query or "open Skype" in query:
            ExelPath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\lync.exe")
            os.startfile(ExelPath)

        elif "open Access" in query or "open access" in query:
            ExelPath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE")
            os.startfile(ExelPath)

        elif "open windows media player" in query:
            qtPath=("C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
            os.startfile(qtPath)

        elif "open Word Pad" in query or "open word pad" in query:
            ExelPath=("C:\\Program Files (x86)\Windows NT\\Accessories\\wordpad.exe")
            os.startfile(ExelPath)

        elif "open powershell" in query or "open Powershell" in query:
            ExelPath=("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")
            os.startfile(ExelPath)

        elif "open snipping tool" in query or "open Snipping Tool" in query:
            ExelPath=("C:\\Windows\\System32\\SnippingTool.exe")
            os.startfile(ExelPath)

        elif "open discord" in query:
            chromePath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chromePath).open_new_tab('https://discord.com/channels/@me')


        elif "open paint" in query or "open Paint" in query:
            ExelPath=("C:\\Windows\\System32\\mspaint.exe")
            os.startfile(ExelPath)

        elif "open maths input tool" in query or "open Math Input Tool" in query:
            ExelPath=("\\CommonProgramFiles\\Microsoft Shared\\Ink\\mip.exe")
            os.startfile(ExelPath)

        elif "open designer" in query:
            qtPath=("C:\\Program Files (x86)\\Qt Designer\\designer.exe")
            os.startfile(qtPath)

        elif "translate" in query:
            langtranslator()

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "top news" in query or "top news headlines" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&apiKey=0945d2e667f9490399058c5010ba80a4")
                data = json.load(jsonObj)
                i = 1

                speak("HEre are some headlines")
                print("==============US TOP NEWS HEADLINES========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif "health news" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=0945d2e667f9490399058c5010ba80a4")
                data = json.load(jsonObj)
                i = 1

                speak("HEre are some headlines")
                print("==============US HEALTH NEWS HEADLINES========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif "sports news" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=0945d2e667f9490399058c5010ba80a4")
                data = json.load(jsonObj)
                i = 1

                speak("HEre are some headlines")
                print("==============US SPORTS NEWS HEADLINES========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif "business news" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0945d2e667f9490399058c5010ba80a4")
                data = json.load(jsonObj)
                i = 1

                speak("HEre are some headlines")
                print("==============US BUSINESS NEWS HEADLINES========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif "entertainment news" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=0945d2e667f9490399058c5010ba80a4")
                data = json.load(jsonObj)
                i = 1

                speak("HEre are some headlines")
                print("==============US ENTERTAINMENT NEWS HEADLINES========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif "tech news" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=0945d2e667f9490399058c5010ba80a4")
                data = json.load(jsonObj)
                i = 1

                speak("HEre are some headlines")
                print("==============US TECH NEWS HEADLINES========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif "sci-fi news" in query or "science news" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=0945d2e667f9490399058c5010ba80a4")
                data = json.load(jsonObj)
                i = 1

                speak("HEre are some headlines")
                print("==============US SCI-FI NEWS HEADLINES ========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))
    
        elif "top news headlines" in query or "headlines" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=0945d2e667f9490399058c5010ba80a4")
                data = json.load(jsonObj)
                i = 1

                speak("HEre are some headlines")
                print("==============US SCI-FI NEWS HEADLINES ========="+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "tell me a joke" in query:
            jokes()
    

        elif "open my inbox" in query:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")

        elif "open whatsapp" in query or "open whats app" in query:
            whatsappPath=("C:\\Users\\Toshiba\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            os.startfile(whatsappPath)

        elif "close whatsapp" in query:
            whatsappPat=("C:\\Users\\Toshiba\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            os.system("TASKKILL /f /IM WhatsApp.exe")

        elif "quit" in query or "bye" in query:
            speak(f"Thank you {name} for giving your time, have a good Day")
            speak("closing engine")
            speak("closing required applications")
            endTime = int(datetime.datetime.now().hour)
            playsound.playsound("power down.mp3")
            rainmeterPath=("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
            os.system("TASKKILL /f /IM Rainmeter.exe")
            quit()

        elif "type" in query:
            speak(f"okay i am listening speak{name} {gender}")
            pyautogui.typewrite(takeCommand())


        elif "search in google" in query:
            speak("what should i search")
            search_Term = takeCommand().lower()
            speak("searching...")
            webbrowser.open('https://www.google.com/search?q='+search_Term)

            
        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif "date" in query:
            date()

        elif 'decrease ' in query:
            print('ok listen.......')
            dec = wmi.WMI(namespace='wmi')
            methods = dec.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(30, 0)
        
        elif 'increase ' in query:
            print('ok listen.......')
            ins = wmi.WMI(namespace='wmi')
            methods = ins.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(100, 0)

        elif "select all" in query:
            pyautogui.hotkey('ctrl','a')

        elif "close this window" in query:
            pyautogui.hotkey('alt','f4')

        elif "open a new tab" in query:
            pyautogui.hotkey('ctrl','n')

        elif "open a new incognito window" in query:
            pyautogui.hotkey('ctrl','shift','n')

        elif "take screenshot" in query:
            Screenshot()

        elif "enter" in query:
            pyautogui.hotkey('ENTER')

        elif "open tab 1" in query:
            pyautogui.hotkey('ctrl','1')

        elif "open tab 2" in query:
            pyautogui.hotkey('ctrl','2')

        elif "new tab" in query:
            pyautogui.hotkey('ctrl','T')

        elif "sleep" in query:
            pyautogui.hotkey('win','M','alt','f4','up arrow','enter')


        elif "copy" in query:
            pyautogui.hotkey('ctrl','c')
            speak('text copied to clipboard')

        elif "paste" in query:
            pyautogui.hotkey('ctrl','v')

        elif "refresh" in query:
            pyautogui.hotkey('f5')

        elif "undo" in query:
            pyautogui.hotkey('ctrl','z')

        elif "redo" in query:
            pyautogui.hotkey('ctrl',)

        elif "change to next window" in query or "next window" in query:
            pyautogui.hotkey('alt','tab')

        elif "find" in query:
            pyautogui.hotkey('ctrl','f')

        elif "back space" in query:
            pyautogui.hotkey('backspace')

        elif "previous window" in query:
            pyautogui.hotkey('L alt','shift ','tab')

        elif "save" in query:
            pyautogui.hotkey('ctrl','s')

        elif "close tab" in query:
            pyautogui.hotkey('ctrl','w')

        elif "back" in query:
            pyautogui.hotkey('browserback')

        elif "go up" in query:
            pyautogui.hotkey('pageup') 

        elif "go to top" in query:
            pyautogui.hotkey('home')

        elif "introduce yourself" in query:
            speak("Let me Introduce my self I am Jarvis an virtual artificial Intelligence made by mohamed saqib from Sunrise English Private Schools. And I am here to assist you with a varaity of task as best i can. 24 hours a day 7 days a week.")

        elif "thank you" in query:
            speak("your welcome sir")

        elif "open cmd" in query:
            os.system("start cmd")

        elif "shutdown" in query:
            speak("do you really want to shutdown")
            reply = takeCommand()
            if "yes" in reply:
                speak("shutting down your laptop")
                os.system("shutdown /s /t 1")
            else:
                break

        elif "restart" in query:
            speak("do you really want to restart")
            reply = takeCommand()
            if "yes" in reply:
                speak("sir i am restarting your laptop")
                os.system("shutdown /r /t 1")
            else:
                break

        elif "log out" in query:
            speak("do you really want to logout")
            reply = takeCommand()
            if "yes" in reply:
                speak("sir logging out")
                os.system("shutdown -l")
            else:
                break

        elif "open code" in query or "vs code" in query:
            speak("Opening code")
            codePath=("C:\\Users\\ohamm\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(codePath)

        elif "open steam" in query:
            codePath=("C:\\Program Files (x86)\\Steam\\Steam.exe")
            os.startfile(codePath)
        
        elif "close steam" in query:
                codePath=("C:\\Program Files (x86)\\Steam\\Steam.exe")
                os.system("TASKKILL /f /IM Steam.exe")

        elif "close code" in query or "close vscode" in query:
                speak("sir i am closing zoom")
                codePath=("C:\\Users\\Toshiba\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                os.system("TASKKILL /f /IM code.exe")

        elif "bandicam" in query:
                codePath=("C:\\Program Files (x86)\\Bandicam\\bdcam.exe")
                os.startfile(codePath)

        elif "close bandicam" in query:
                codePath=("C:\\Program Files (x86)\\Bandicam\\bdcam.exe")
                os.system("TASKKILL /f /IM bdcam.exe")

        elif "stop listening" in query:
            speak('for how many second you want me to stop listening to your commands')
            ans = int(takeCommand())
            time.sleep(ans)
            print(ans)


        #elif 'email' in query:
        #    try:
        #        speak("What should I say?")
         #       content = takeCommand()
         #       to = "mohamedsaqibjaveed@gmail.com"    
          #      sendEmail(to, content)
           #     speak("Email has been sent!")
            #except Exception as e:
             #   print(e)
              #  speak("Sorry my friend . I am not able to send this email")    

        #elif "email" in query:

##             email = 'saqibjaveed2006@gmail.com' 
  #              password = 'j@veed77'
   #             send_to_email = 'javeednoorullah@gmail.com'
    #            query = takeCommand().lower() 
     #           subject = query
      #          speak("what is the message for the email")
       #         query2 = takeCommand().lower()
        #        Message = query2
         #       speak("sir put the file path u want to send")
          #      file_location = input("Please Enter The Path Here")
#
 #               speak("Sir, Please Wait I Am Sending The Email")
#
 #               msg  = MIMEMultipart()
  #              msg['From'] = email
   #             msg['To'] = send_to_email
    #            msg['subject'] = subject
#
 #               msg.attach(MIMEText(Message, 'plain'))
#
 #               filename = os.path.basename(file_location)
  #              attachment = open(file_location, "rb")
   #             part = MIMEBase('application', 'octet-stream')
    #            part.set_payload(attachment.read())
     #           encoder.encode_base64(part)
      #          part.add_header('content-disposition', "attachment; filename= %s" % filename)
#
#
 #               msg.attach(part)
#
 #               server = smtplib.SMTP('smtp.gmail.com', 587)
  #              server.ehlo()
   #             server.starttls()
    #            server.login('saqibjaveed2006@gmail.com', 'j@veed77')
     #           server.sendmail(email, send_to_email, Message)
      #          server.close()
#

        elif 'email' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "8501@seps-auh.org"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend . I am not able to send this email")    


        elif "english" in query:
            sign_in('2081547566','7wV7dK')

        elif "hindi" in query:
            sign_in('3802428421','9N3ssx')

        elif "sst" in query:
            sign_in('6694404278','1UpTgU')

        elif "phe" in query:
            sign_in('6332574812','PHE123')

        elif "Art" in query:
            sign_in('9512561176','1gbJt3')

        elif "islamic" in query:
            sign_in('7435439592','TPJ@20')

        elif "usst" in query:
            sign_in('2285299594','9nyj8c')

        elif "sir" in query:
            sign_in('6182051710','7rkzht')

        elif "mam" in query:
            sign_in('2750812926','9dsVmf')

        elif "computer" in query:
            sign_in('4555602366','6E8YVy')

        elif "arabic" in query:
            sign_in('7573823734','7PtymV')

        elif "bio" in query:
            sign_in('9948316784','139568')

        elif "chemistry" in query:
            sign_in('9856554349','1rn4Zf')

        elif "physics" in query:
            sign_in('8465321592','5ruRvm')

        