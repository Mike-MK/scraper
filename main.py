from msilib.schema import ListBox
from typing import OrderedDict
from bs4 import BeautifulSoup
import requests
import re
import pprint as pprint

from requests.api import get

from tkinter import *
from tkinter import ttk

max_width=1000
max_height=500
window = Tk()
window.title("Web scrapper")
window.maxsize(max_width,max_height)
window.config(bg='white')

def get_words(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,features='html.parser')
    words = []
    diction= OrderedDict()
    for string in soup.stripped_strings:
        line = re.split(' |;|\n|@|\.,',string)
        for i in line:
            words.append(i.lower())

    words = sorted(words)

    for word in words:
        if word in diction.keys():
            diction[word]+=1
        else:
            diction[word] = 1
    return diction  

def run():
    url_1 = url_entry.get()
   
    if not url_1:
        return

    results_1 = get_words(url_1) if url_1 else ''

    try:      
        for key in results_1.keys():
            lbox_1.insert(END, f"{key}: {results_1[key]}")
        
    except Exception as e:
        print(e)
    
  
UI_frame = Frame(window, width=1000, height=500, bg='white')
UI_frame.pack(side=TOP,padx=10,pady=10)


l1= Label(UI_frame,text='Enter url:')
l1.pack(side=TOP,padx=5,pady=5)

url_entry = Entry(UI_frame,fg='black',bg='white',width=500)
url_entry.pack(side=TOP)

lbox_1 = Listbox(UI_frame,width=500)
lbox_1.pack(side=TOP,fill=BOTH)

btn_run = Button(UI_frame,bg='white',width=50,text='Run',command=run)
btn_run.pack(side=BOTTOM)

window.mainloop()