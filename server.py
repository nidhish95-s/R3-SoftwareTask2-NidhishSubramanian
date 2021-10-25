import socket
config_1 = [    ["f","f","f","f"],
                ["r","r","r","r"],
                ["r","r","f","f"],
                ["f","f","r","r"],
                ["n","n","n","n"],
                ["T","W","R","K"]   ]   #rover movement matrix.

motor_dir = ["w","s","a","d","x","z"]    # key binding matrix.   
moto_drive = ["n","n","n","n"] #pre-initialize.
speed = "0" #pre-initialize.
con = 1 #for the while loop.
print("""

    Few things to note.
    - Hitting left control will kill the client.
    - Hitting space will kill the server.
    - You can set speed or direction first. Doesn't matter.
    - "n" is for neutral.
    - When in neutral, wheels will continue to spin, so look at the previous heading
    - to know where you''re going.
    - To go back to neutral, hit x.
    - The rover turns on as you connect to the server and turns off as you disconnect.
    - Speeds ranges from 0-5.
    - Press w to move forward, s to move backwards, a for left and d for right.
    - Input is case sensitive, AVOID CAPS.
    - Hit enter to see current heading. 
    - Hit z for Rover to perform a dance move you can't see. 
    - Dance speed can be adjusted using the buttons mentioned above.
        
    """)
def rover_out(message): #take in message from client.
    global speed, moto_drive  #make speed and direction variables global.This allows stops it from reverting to its default value(s).
    while con == 1:        
        
        user_input = str(message) #cast input into a string variable.                   
        for x in motor_dir:                    
            if user_input == x:
                index = motor_dir.index(x)   #mark down where the match happened                          
                for i in range(4): # range of 4 because everything is limited to 4.
                    moto_drive[i] = config_1[index][i]   #change the default drive direction to the one from the movement matrix.                                  
        for x in range(len(config_1)):     #now setting speed                  
            x = str(x)     #cast it to a string.            
            if user_input == x:            
                x = (int(x)/5) * 255 #convert to PWM value.
                speed = str(x)  #for contancotancontantacatation.                                                           
        for x in range(1): #There's a better way to do this :((
            print("["+moto_drive[x]+speed+"]"+"["+moto_drive[x+1]+speed+"]"+"["+moto_drive[x+2]+speed+"]"+"["+moto_drive[x+3]+speed+"]")                                    
        return 0
        
               
                           

s_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1' #local host
port = 1255 #random number. Did not see which ports were open/occupied.
s_soc.bind((host,port)) #as it says, we bind our server to this port. The client will "meet" us here? (i think that's how it works)
s_soc.listen(2) #we can take 2 if we want to.
clientmessage, clientaddress = s_soc.accept()

connection = True
while connection:
    message = clientmessage.recv(1024) #buffer for the message size
    message = message.decode(("utf-8")) #because I saw this in a tutorial. But this is how data is sent, so we must decode it.
    rover_out(message)    
    if message == "Key.space": #disconnection cue
        connection = False
        s_soc.close()    #close connection.
    