import os
from tkinter import *
from tkinter.messagebox import *
from main import set_homepage

def first_interface():
    master=Tk()
    master.title("WEB SCRAPER")
    label=Label(master, text="ENTER THE URL" ,relief="groove", width=19)
    name=Entry(master)
    
    def start_second_interface():
        site=str(name.get())
        HOMEPAGE=site
        os.system('main.py')
        print(HOMEPAGE)
    main_button=Button(master, text="SCRAPE", relief="groove", width = 21 , command= start_second_interface)
    '''label.grid(row=1,column=1,padx=10)
    name.grid(row=1, column=2, padz=10)
    main_button.grid(row=2,column=1,padx=10)'''
    label.pack()
    name.pack()
    main_button.pack()
    master.mainloop()
first_interface()
