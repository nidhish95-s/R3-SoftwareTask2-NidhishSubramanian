# R3-SoftwareTask2-NidhishSubramanian

Both the video files open when clicking view raw. 

Essentially, used a movement matrix to configure the motors.

And based on the keys entered from the keyboard and using simple "statements"

determined which row and column of movement matrix to use for the motors.

Speed settings were straight forward and since we had a limitation of either forward, left, right or backward movement

with the speed setting going from 0 to 5, using the size of the movement matrix to indirectly set the speed worked.

I am sorry if this readme isn't more in depth, but there is a lot I don't know about sockets. But from what I did for this package,

I can say that the local host address and IP address are not the same. One is used to loop back to the same pc, the other is used to go out locally.

Also, ports are either taken by other networks or are not used by the computer, so typing a random number might work, but it is better to know what's open

and closed. Also, I did a keylogging exercise on the side to learn how to monitor the keyboard. It was not pertinent to this project, so I didn't 

use a text file to control the rover. Although it could have worked, like sending an indirect message that could also be accessed by other clients if needed. 

But that's how I learned how to use the controller, using pynput. 

The rover works as intended. I wrote in an extra TWRK row in the movement matrix, that I imagine will make the rover twerk. Speed settings work for this twerk mode as  well.

It basically spits out [T255][W255][R255][K255]

I imported only socket and Listener from pynput, so if you run my code, it shouldn't need anything else. 
