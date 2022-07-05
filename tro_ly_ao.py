import speech_recognition
import pyttsx3
from datetime import date , datetime

# Phần khởi tạo 
robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
# Phần robot nghe

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot : I'm listening")
		audio = robot_ear.listen(mic)

	print("Robot : ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = " "

	print("You : " + you)


	#Phần robot hiểu
	if you == "hello" or you == "Good morning":
		robot_brain = "Hello My friend "
	elif "time" in you :
		now = datetime.now()
		robot_brain = now.strftime("%H Hours %M Minutes %S Seconds")
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d , %Y")
	elif you == "how are you" :
		robot_brain = "I'm fine , thank you"
	elif "bye" in you:
		robot_brain = "Ok, Goodbye"
		print("Robot : " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "Sorry , Can't you say something" 
	print("Robot : " + robot_brain)


	#Phần Robot nói
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()