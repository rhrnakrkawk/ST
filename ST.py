# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 03:17:15 2023

@author: twoo1
"""


import paho.mqtt.client as mqtt
import threading
import time
from tkinter import *
from tkinter import messagebox
 
class MyFrame(Frame):
    def __init__(self, master=Frame):
        self.lb_dronestate = Label(master, text = "drone state : ")
        self.lb_dronestate.place(x=20, y=100)
        
        self.lb_curdronestate = Label(master, text = "nomal")
        self.lb_curdronestate.place(x=90, y=100)
        
    def sett(self, text1):
        self.lb_curdronestate.config(text=text1)
 

def mqtt_s():
    s_st.loop_forever()
    
def call_back(client, userdata, message):
    string = str(message.payload.decode("utf-8"))
    if(string == "report"):
        msg = messagebox.askquestion("report", "there is report\ndo you start mission?")
        if(msg == "yes"):
            s_st.publish("/data/drone", "go")
            frame.sett("on progress")
    elif(string == "done"):
        messagebox.showinfo("info", "mission clear!")
        frame.sett("no progress")

 
    
if __name__ == '__main__':
    broker = "210.106.192.242"
    s_st = mqtt.Client("mqtt_ST")
    s_st.on_message = call_back
 
    
    s_st.connect(broker, 1883)
    s_st.subscribe("/data/ST")
   
    root = Tk()
    root.title('GUI')
    root.geometry('200x200')
    frame = MyFrame(root)
    
    t2 = threading.Thread(target=mqtt_s)
    t2.start()
    
    root.mainloop()
