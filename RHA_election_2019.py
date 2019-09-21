import pynput, random, time, webbrowser, datetime
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller

mouse = Controller()
keyboard = Controller()

t_end = time.time()+60*60*4

Joe = "" '''insert name1'''
Joe_delay = 1

Tiff = "" '''insert name2'''
Tiff_delay = 3
tiff_time_delay = 0

address = 'https://umasslowell.co1.qualtrics.com/jfe/form/SV_eE6hWXmLRhZLQRT'
url = 'www.google.com'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'


def cast_vote(candidate):
    webbrowser.get(chrome_path).open_new(address)
    
    time.sleep(1)
    
    mouse.position = (-14,30)
    
    time.sleep(1)
    
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab) 
    keyboard.release(Key.tab)
    
    keyboard.type('Joseph McGonagle')
    
    keyboard.press(Key.tab)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(4)
    keyboard.press(Key.ctrl_l)
    keyboard.type('w')
    keyboard.release(Key.ctrl_l)
    
    time.sleep(5)


while(True):
    minute = datetime.datetime.now().minute
    
    if(minute % 2 == 0):
        cast_vote('Joseph McGonagle')
        print("Lowell Analytica cast a vote at", datetime.datetime.now(), "in favor of Joseph McGonagle")
        
    if(minute % 7 == 0):
        cast_vote('Tiffany Powers')
        print("Lowell Analytica cast a vote at", datetime.datetime.now(), "in favor of Tiffany Powers")
    
    time.sleep(60)
        
