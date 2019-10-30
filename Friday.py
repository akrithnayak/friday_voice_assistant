#!/usr/bin/env python
# coding: utf-8

# In[1]:



import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr


# In[ ]:


machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')
machine.setProperty('voice',voices[0].id)

command_list=[]
def speak(audio):
    print("Friday:",audio)
    machine.say(audio)
    machine.runAndWait()
    
def wish():
    
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning bro")
    elif hour >= 12 and hour < 15:
        speak("Good Afternoon bro")
    else:
        speak("Good Evening bro")
    #speak("My name is Friday......how can i help you brother?")
    
def open_site(audio):
    if('Google' in audio):
        webbrowser.open('https://www.google.com')
    elif('YouTube' in audio):
        webbrowser.open('https://www.youtube.com')
        
def communicate(audio):
    if(audio=='what is your name'):
        speak('My name is Friday')
    elif(audio=='how are you'):
        speak('I am fine! How are you?')
    elif('fine' in audio.split()):
        speak('Pleased to hear that bro!')
    elif(audio=='what was my last command'):
        sa=command_list.pop()
        speak("Your last command was:"+sa)
        stack(sa)
    elif(audio=='execute my last command'):
        sa=command_list.pop()
        communicate(sa)
        open_site(sa)
        stack(sa)

#     else:
#         speak(audio)
        

def stack(audio):
    command_list.append(audio)
    
r = sr.Recognizer()  

def takeCommand():

    while(1):
        with sr.Microphone() as source:
            print("Listening....")                                                                                   
            r.pause_threshold = 2
            r.energy_threshold = 150
            audio = r.listen(source)

        try:
            print("Recognising...")
            query = r.recognize_google(audio, language='en-uk')
            print(f"User said: {query}")
            if(query!='what was my last command' and 'execute my last command'):
                stack(query)
            if(query.split()[0]=='open'):
                open_site(query)
            elif(query == 'exit'):
                return
            else:
                communicate(query)
            

        except:
            #query = "Say that again please...."
            speak("Say that again please....")
            
        
            
if __name__ == '__main__':
    wish()
    
    while(1):
        print("Press Enter and say 'Friday' to wake up the assisstant!")
        input()
        with sr.Microphone() as source:
            print("Listening....")                                                                                   
            r.pause_threshold = 1
            r.energy_threshold = 150
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-uk')
            print(f"User said: {query}")
            if query == 'Friday':
                speak("Access granted!!")
                takeCommand()
        except:
            print("Say that again please....")
    
    

