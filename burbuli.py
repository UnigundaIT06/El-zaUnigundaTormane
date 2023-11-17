#Mērķis ir uztaisīt programmu, kurā zemūdene spridzina burbuļus
#Tiek skaitīti punkti

from tkinter import *
from random import *
from math import * 

logs = Tk()
garums = 700
platums = 700
logs.title("Burbuļu spridzinātājs")
a = Canvas(logs, width=platums, height=garums, bg='darkred')
a.pack()
kuga_id2 = a.create_oval(5,5,100,100, outline='darkgreen', width=10)




mainloop()







