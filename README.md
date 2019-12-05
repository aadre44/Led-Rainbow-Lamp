# Led-Rainbow-Lamp
3D printed Pine cone lamp that uses Led lights with programmed animations controlled through wifi!
The lamp is 3D printed out of PLA from a 3D model that can be found online on Thingy verse. I used clear PLA plastic when printing the model so that the light can shine through the model brightly with a diffused look so the colors blend together nicely.
A Raspberry Pi Zero W is used to control the 60 pixel ws281b led light strip with either a button glued to the back of the lamp or wirelessly through a web server

To run the code you have to start the flask server from the flaskTest.py python file first and then run ledControl.py.
On the raspbery pi (rpi) I wanted this to automatically happen when the rpi turns on so I made a shell scripts to run on start up that
runs the flask server then starts the led python script. Wiring diagram and video are in the demo folder.
