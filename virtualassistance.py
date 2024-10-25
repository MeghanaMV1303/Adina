from http.client import HTTP_VERSION_NOT_SUPPORTED
from matplotlib.dates import HOURLY, HOURS_PER_DAY, HourLocator
import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import wikipedia 
import pyjokes

def takeCommand():

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Listening')
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		
		try:
			print("Recognizing")
			 
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"		
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()

	voices = engine.getProperty('voices')
	
	
	engine.setProperty('voice', voices[0].id)
	
	engine.say(audio) 
	

	engine.runAndWait()

def tellDay():
	
	
	day = datetime.datetime.today().weekday() + 1
	
	
	Day_dict = {1: 'Monday', 2: 'Tuesday', 
				3: 'Wednesday', 4: 'Thursday', 
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	

	time = str(datetime.datetime.now())
	
	
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak("The time is sir" + hour + "Hours and" + min + "Minutes") 



def Hello():
	
	
	speak("hello Meghana I am your desktop assistant Adina . Tell me how may I help you")




def Take_query():

	
	Hello()
	
	
	while(True):
		
		
		query = takeCommand().lower()
		if "open geeksforgeeks" in query:
			speak("Opening GeeksforGeeks ")
			
			
			webbrowser.open("www.geeksforgeeks.com")
			continue
		
		elif "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
		elif "i love you" in query:
			speak("It's hard to understand")
			continue
		elif "will you be my gf" in query or "will you be my bf" in query:  
			speak("I'm not sure about, may be you should give me some time")
			continue
		elif "how are you" in query:
			speak("I'm fine, glad you me that")
			continue
		elif 'reason for you' in query:
			speak("I was created as a Minor project by Miss Meghana MV ")
			continue
		elif "who i am" in query:
			speak("If you talk then definitely your human.")
		elif "why you came to world" in query:
			speak("Thanks to Meghana. further It's a secret")
		elif 'reason for you' in query:
			speak("I was created as a Minor project by Miss Meghana MV ")
		elif 'joke' in query:
			speak(pyjokes.get_joke())
		elif "i love you" in query:
			speak("It's hard to understand")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")
		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")
		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query
		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")
		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)
		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")
			continue
		elif "which day it is" in query:
			tellDay()
			
		elif "tell me the time" in query:
			tellTime()
			continue
			
		elif "Good Morning" in query:
			speak("A warm")
			
			
		elif "bye" in query:
			speak("Bye. Check Out GFG for more exciting things")
			exit()

		
		elif "from wikipedia" in query:
			
			
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)
		
		elif "tell me your name" in query:
			speak("I am Adina. Your desktop Assistant")

if __name__ == '__main__':
	
	Take_query()

