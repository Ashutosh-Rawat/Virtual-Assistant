from inputFile import speech_to_text
from processFile import process
from outputFile import output
from cmdInput import take_input
import os
import assistantDetails as ad
from database import listen_is_on

if ad.is_ubuntu():
	os.system('clear')
else:
	os.system('cls')

output("Welcome User! I am your personal assistant. How can I help you?")
while(True):
    if listen_is_on():
        i = speech_to_text()
    else:
        i = take_input()
    o = process(i)
    output(o)
