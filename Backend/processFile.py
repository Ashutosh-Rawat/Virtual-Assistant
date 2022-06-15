from internet import check_on_wikipedia
from inputFile import speech_to_text
from outputFile import output
import random
import os
from web import open_facebook, open_google, close_browser, search_google, search_youtube
from weather import check_weather
from database import *
from timeDetails import get_time, get_date
from news import get_news
from calculator import calculator
from AIBot import response
import wikipedia

def  process(query):
    noAnswer = ["Sorry, I can't understand you", "Please give me more info", "I am not sure I understood it", "Can you ask again please", "I am very sorry but I can't understand you"]

    
    if len(query)<=1:
        return random.choice(noAnswer)
    
    if 'quit' in query:
        output('Thank you!!! See You Soon')
        exit()
    
    if query == 'weather' in query:
        answer = get_answer_from_memory('location')
    
    elif 'search' in query:
        answer = get_answer_from_memory('search')
    
    elif 'calculate' in query:
        answer = get_answer_from_memory('calculate')
        
    elif 'map' in query:
        answer = get_answer_from_memory('google map')
        
    elif 'who' in query:
        cmd = query.lower()
        answer = wikipedia.summary(cmd, sentences=2)
        if answer != '':
            return answer
        else:
            return 'no info found'
    
    else:
        answer = get_answer_from_memory(query)
    

    if answer == 'get time details':
        return('Time is '+get_time()+' and date is '+get_date())
    
    elif answer == 'open facebook':
        open_facebook()
        return "opening facebook"
    
    elif answer == 'close browser':
        close_browser()
        return "closing browser"
    
    elif answer == 'check internet connection':
        if check_internet_connection():
            return 'internet connection is on'
        else:
            return 'internet connection is off'
        
    elif answer == 'search':
        if 'youtube' in query:
            query = query.replace('search', '')
            query = query.replace('on youtube', '')
            search_youtube(query)
            return 'searching on youtube'
        else:
            query = query.replace('search', '')
            query = query.replace('google', '')
            query = query.replace('on google', '')
            search_google(query)
            return 'searching on google'
        
    elif answer == 'get news':
        return get_news()
    
    elif answer == 'weather':
        place = query.replace('weather', '')
        return check_weather(place)
    
    elif answer == 'calculate':
        return calculator(query)
    
    elif answer == 'map':
        index = query.lower().split().index('map')
        question = query.split()[index+1:]
        cmd = 'python map.py ' + ' '.join(question)
        os.system(cmd)
        return 'opening google maps'
    
    else:
        res = response(query)
        if res != '0':
            return res
        
        else:
            output("I don't know this, should I search it over internet?")
            ans = speech_to_text()
            if 'yes' in ans:
                output('searching on wikipedia...')
                answer = check_on_wikipedia(query)
                if answer != '':
                    return answer
                
            else:
                output('can you please explain about that?')
                answer = speech_to_text()
                if 'it means' in answer:
                    answer = answer.replace('it means', '')
                    answer = answer.strip()
                    
                    value = get_answer_from_memory(ans)
                    
                    if value == '':
                        return "can't help with this one"
                    
                    else:
                        insert_question_and_answer(query, value)
                        return 'thanks, I will remember that'
                    
                else:
                    return "can't help with this one"
                    
    return 'nothing'
    