from timeDetails import get_hours, get_date
from outputFile import output
from database import update_last_seen, get_last_seen
import assistantDetails as ad
from datetime import date
from inputFile import speech_to_text

def greet(status):
	speech_to_text("Hello user, I am your personal assistant. How can I help you?")
	#fetch previous date 
	previous_date = get_last_seen()
	#fetch today's date and store it to database 
	today_date = get_date()
	update_last_seen(today_date)

	bot = ad.name
	m = "Here are a few popular actions."
	msg = ". Your " + bot + " the Virtual Assistant here. There's a lot I can help with. " + m

	if previous_date == today_date:
		output("Welcome back "+status+msg)
	else:
		hour = int(get_hours())
		if (hour >= 4 and hour <12 ):
			output("Good Morning, "+status+msg)
		elif (hour >= 12 and hour <16 ):
			output("Good Afternoon, "+status+msg)
		else:
			output("Good Evening, "+status+msg)
	

