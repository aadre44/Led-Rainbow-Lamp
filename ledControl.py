from rpi_ws281x import *
import time
import sys
import RPi.GPIO as GPIO 
import requests
import subprocess
import _thread
import flaskTest
import random

"""
RPI GPIO setup 
"""
buttonPin = 10
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

"""
Global Variables
returned - used for animations to keep track if something is returned. If so that means animation is mid animation
btnPress - used to know if a button was pressed during the animation script
mode - represents the current mode in the cycle
url - url to the http server
httpCHange - 
enc - Error. No. Connection.: used to count the number of tries connecting to http web server. At 5 trying is stopped
"""
returned = None
btnPress = False
mode = -1
url = "http://192.168.0.27:5000"
httpChange = False
enc = 0
firstConnect = True


"""
Led Global Variables and led setup
"""
ledCount = 60
ledPin = 18
ledFreq = 800000
ledDma = 10
ledBrite = 255
ledInvert = False
ledChannel = 0

led = Adafruit_NeoPixel(ledCount, ledPin, ledFreq, ledDma, ledInvert, ledBrite,ledChannel)
led.begin()


"""setColor
Sets all leds to the same color given in the parameters. 
Parameter1- number of leds to be used 
Parameter2- tuple of 3 ints to represent RGB values of color of led
"""
def setColor(leds = 5, color = (255, 0, 0)):
	for i in range(0, leds):
		led.setPixelColor(i, Color(color[0],color[1],color[2]))
		
	led.show()

"""setColorW
Sets all leds to the same color given in the parameters. 
Parameter1- number of leds to be used 
Parameter2- string representing the color
"""
def setColorW(leds = 5, color = "WHITE", b = 1):
	rgb = (0,0,0)
	if(color == "WHITE"):
		rgb = (int(100/b), int(255/b),int(255/b))
	elif(color == "WARM"):
		rgb = (255,255,255)
	elif(color == "RED"):
		rgb = (255,0,0)
	elif(color == "GREEN"):
		rgb = (0,255,0)
	elif(color == "BLUE"):
		rgb = (0,0,255)
	elif(color == "PINK"):
		rgb = (255,0,255)
	elif(color == "CLEAR"):
		rgb = (0,0,0)
	   
	for i in range(0, leds):
		led.setPixelColor(i, Color(rgb[0],rgb[1],rgb[2]))
		
	led.show()

"""setRainbow
Sets all leds to shift through the color wheel from 0-parameter1. 
Parameter1- number of leds to be used 
"""
def setRainbow(leds = 60):
	leds = leds
	valueUp = 255
	valueDown = 0
	position = 0
	step = transition(leds)
	for i in range(0, leds):
		valueUp -= step
		valueDown += step
		if valueDown >= 255:
			valueUp = 255 - step
			valueDown = 0 + step
			position += 1
		if position == 0:
			led.setPixelColor(i, Color(valueUp,valueDown,0))
		else:
			led.setPixelColor(i, Color(0,valueUp,valueDown))
	
	led.show()


""" Transition
Finds the step size so that from led 0 to led total you will reach every 
color of the rainbow
Parameter1- number of leds to be used 
"""
def transition(total = 10, position = 0):
	step = int(255*2/total)
	return step

"""breathe
Breathe animation
Parameter1- number of leds to be used
Parameter2- tuple of 3 ints to represent RGB values of color of led 
Parameter3- int value representing speed of breathe animation
"""
def breathe(leds = 60, color = (0,0,0), speed = 0):
	for i in range(0, 150):
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,i))
		led.show()
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			return
		time.sleep(.05)
	print("GOING DOWN")
	for i in range(0, 150):
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,150-i))
		led.show()
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! DOWN")	
			btnPress = True
			return
		time.sleep(.05)

"""breathe 2
Breathe animation
Parameter1- number of leds to be used
Parameter2- tuple of 3 ints to represent RGB values of color of led 
Parameter3- int value representing speed of breathe animation
"""
def breathe2(leds = 60, color = (0,0,0), speed = 0):
	for i in range(0, 150):
		for j in range(0, int(leds/3)):
			led.setPixelColor(j, Color(0,0,i))
		for k in range(int(leds/3), leds):
			led.setPixelColor(k, Color(i,0,0))
		led.show()
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			return
		time.sleep(.05)
	print("GOING DOWN")
	for i in range(0, 150):
		for j in range(0, int(leds/3)):
			led.setPixelColor(j, Color(0,0,150-i))
		for k in range(int(leds/3), leds):
			led.setPixelColor(k, Color(150-i,0,0))
		led.show()
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! DOWN")	
			btnPress = True
			return
		time.sleep(.05)

"""breathe 3
Breathe animation
Parameter1- number of leds to be used
Parameter2- tuple of 3 ints to represent RGB values of color of led 
Parameter3- int value representing speed of breathe animation
"""
def breathe3(leds = 60, info = None, color = (0,0,0), speed = 0):
	global returned
	if(info == None):
		for i in range(0, 150):
			for j in range(0, int(leds/3)):
				led.setPixelColor(j, Color(0,0,1+i))
			for k in range(int(leds/3), leds):
				led.setPixelColor(k, Color(1+i,0,0))
			led.show()
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				return
			time.sleep(.05)
		returned = 1
	else:
		if(info == 1):
			for i in range(0, 150):
				for j in range(0, int(leds/3)):
					led.setPixelColor(j, Color(0,1+i,150-i))
				for k in range(int(leds/3), leds):
					led.setPixelColor(k, Color(150-i,0,1+i))
				led.show()
				if GPIO.input(10) == GPIO.HIGH:
					print("Button was pushed! ")	
					btnPress = True
					return
				time.sleep(.05)
			
			returned = 2
		if(info == 2):
			for i in range(0, 150):
				for j in range(0, int(leds/3)):
					led.setPixelColor(j, Color(1+i,150-i,0))
				for k in range(int(leds/3), leds):
					led.setPixelColor(k, Color(0,1+i,150-i))
				led.show()
				if GPIO.input(10) == GPIO.HIGH:
					print("Button was pushed! ")	
					btnPress = True
					return
				time.sleep(.05)
			
			returned = 3
		if(info == 3):
			for i in range(0, 150):
				for j in range(0, int(leds/3)):
					led.setPixelColor(j, Color(150-i,0,1+i))
				for k in range(int(leds/3), leds):
					led.setPixelColor(k, Color(1+i,150-i,0))
				led.show()
				if GPIO.input(10) == GPIO.HIGH:
					print("Button was pushed! ")	
					btnPress = True
					return
				time.sleep(.05)
			
			returned = 1
		
		
	

"""Wave
Wave animation
Parameter1- number of leds to be used
Parameter2- tuple of values representing where in the animation to start
"""	
def wave(leds = 60, info = None):
	global returned 
	step = transition(leds)
	if( info == None):
		valueUp = 255
		valueDown = 0
		position = 0
		
		for i in range(0, leds):
			valueUp -= step
			valueDown += step
			if valueDown >= 255:
				valueUp = 255 - step
				valueDown = 0 + step
				position += 1
			if position == 0:
				led.setPixelColor(i, Color(valueUp,valueDown,0))
			else:
				led.setPixelColor(i, Color(0,valueUp,valueDown))
		
		led.show()
	else:
		valueUp = info[0]
		valueDown = info[1]
		position = info[2]

	print("waving")
	for i in range(0, leds):
		valueUp -= step
		valueDown += step
		if valueDown >= 255:
			valueUp = 255 - step
			valueDown = 0 + step
			position += 1
			if(position > 2):
				position = 0
		if position == 0:
			led.setPixelColor(i, Color(valueUp,valueDown,0))
		elif position == 1:
			led.setPixelColor(i, Color(0,valueUp,valueDown))
		else:
			led.setPixelColor(i, Color(valueDown,0,valueUp))
				
		led.show()
		time.sleep(.05)
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			break
			
	returned = (valueUp, valueDown, position)

"""Changing
Changing animation
Parameter1- number of leds to be used
Parameter2- tuple of values representing where in the animation to start
"""	
def changing(leds = 60, info = None):
	
	global returned 
	step = transition(leds)
	if( info == None):
		valueUp = 255
		valueDown = 0
		position = 0
	else:
		valueUp = info[0]
		valueDown = info[1]
		position = info[2]
	
	
	
	print("changing")
	for i in range(0, leds):
		valueUp -= step
		valueDown += step
		if valueDown >= 255:
			valueUp = 255 - step
			valueDown = 0 + step
			position += 1
			if(position > 2):
				position = 0
		if position == 0:
			led.setPixelColor(i, Color(valueUp,valueDown,0))
		elif position == 1:
			led.setPixelColor(i, Color(0,valueUp,valueDown))
		else:
			led.setPixelColor(i, Color(valueDown,0,valueUp))
		
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			returned = None
			return
			#break
		
	led.show()

	for i in range(0,10):
		time.sleep(.1)
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			returned = None
			return
	
	returned = (valueUp, valueDown, position)

"""shift
shift animation
Parameter1- number of leds to be used
Parameter2- tuple of values representing where in the animation to start
"""	
def shift(leds = 60, info = None):

	print("shifting")
	global returned 
	step = transition(leds)
	if( info == None):
		valueUp = 255
		valueDown = 0
		position = 0
		x = 0
	else:
		valueUp = info[0]
		valueDown = info[1]
		position = info[2]
		x = info[3]
		
	if(x > leds):
		x=0
		
	for i in range(0, x):
		valueUp -= step
		valueDown += step
		if valueDown >= 255:
			valueUp = 255 - step
			valueDown = 0 + step
			position += 1
			if(position > 2):
				position = 0
		if( i%3 == 0):
			if position == 0:
				led.setPixelColor(i, Color(valueUp,valueDown,0))
			elif position == 1:
				led.setPixelColor(i, Color(0,valueUp,valueDown))
			else:
				led.setPixelColor(i, Color(valueDown,0,valueUp))
			print("index "+str(i)+" position "+ str(position))
		else:
			if position == 1:
				led.setPixelColor(i, Color(valueUp,valueDown,0))
			elif position == 0:
				led.setPixelColor(i, Color(0,valueUp,valueDown))
			else:
				led.setPixelColor(i, Color(valueDown,0,valueUp))
			print("index "+str(i)+" position "+ str(position))
				
			
		led.show()
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			break
		time.sleep(.05)
		
	for i in range(x, leds):
		valueUp -= step
		valueDown += step
		if valueDown >= 255:
			valueUp = 255 - step
			valueDown = 0 + step
			position += 1
			if(position > 2):
				position = 0
		if( i%3 == 0):
			if position == 0:
				led.setPixelColor(i, Color(valueUp,valueDown,0))
			elif position == 1:
				led.setPixelColor(i, Color(0,valueUp,valueDown))
			else:
				led.setPixelColor(i, Color(valueDown,0,valueUp))
			print("index "+str(i)+" position "+ str(position))
		else:
			if position == 1:
				led.setPixelColor(i, Color(valueUp,valueDown,0))
			elif position == 0:
				led.setPixelColor(i, Color(0,valueUp,valueDown))
			else:
				led.setPixelColor(i, Color(valueDown,0,valueUp))
			print("index "+str(i)+" position "+ str(position))
			
		led.show()
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			break
		time.sleep(.05)
		
	x += 1
		
		
	led.show()
	time.sleep(.05)
	returned = (valueUp, valueDown, position, x)

"""shiftSolid
shiftSolid animation
Parameter1- number of leds to be used
Parameter2- tuple of values representing where in the animation to start
"""	
def shiftSolid(leds = 60, info = None):
	
	print("shifting Solid")
	global returned 
	step = transition(leds)
	if( info == None):
		valueUp = 255
		valueDown = 0
		position = 0
		x = 0
		y = 0
		setColorW(60, "BLUE")
	else:
		valueUp = info[0]
		valueDown = info[1]
		position = info[2]
		x = info[3]
		y = info[4]
		
	if(x > leds):
		x=0
		
	if(y != 0):
		step = 1
	
	for i in range(0, x):
		valueUp -= step
		valueDown += step
		if valueDown >= 255:
			valueUp = 255 - step
			valueDown = 0 + step
			position += 1
			if(position > 2):
				position = 0
		if position == 0:
			led.setPixelColor(i, Color(valueUp,valueDown,0))
		elif position == 1:
			led.setPixelColor(i, Color(0,valueUp,valueDown))
		else:
			led.setPixelColor(i, Color(valueDown,0,valueUp))
		print("index "+str(i)+" position "+ str(position))
			
		led.show()
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			break
		time.sleep(.15)
		
	for i in range(x, leds):
		valueUp -= step
		valueDown += step
		if valueDown >= 255:
			valueUp = 255 - step
			valueDown = 0 + step
			position += 1
			if(position > 2):
				position = 0
		if position == 0:
			led.setPixelColor(i, Color(valueUp,valueDown,0))
		elif position == 1:
			led.setPixelColor(i, Color(0,valueUp,valueDown))
		else:
			led.setPixelColor(i, Color(valueDown,0,valueUp))
		
		print("index "+str(i)+" position "+ str(position)+ "up "+str(valueUp)+"down "+str(valueDown))
		
		led.show()
		if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			break
		time.sleep(.15)

	x += 1
	y+=1
	led.show()
	print("set updating up: "+str(valueUp))
	if GPIO.input(10) == GPIO.HIGH:
			print("Button was pushed! ")	
			btnPress = True
			return
	time.sleep(.35)
	returned = (valueUp, valueDown, position, x, y)

"""notify
notify animation
Parameter1- number of leds to be used
Parameter2- tuple of values representing where in the animation to start
Parameter1- number of leds you want to use
Parameter2- tuple of values representing where in the animation to start
"""	
def notify(leds = 60, num = 0, info = None, color = (0,0,0)):
	if num == 0:
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,255))
		led.show()
		for i in range(0,5):
			time.sleep(.1)
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				returned = None
				return
		
			
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,0))
		led.show()
		for i in range(0,5):
			time.sleep(.1)
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				returned = None
				return
		
		
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,255))
		led.show()
		for i in range(0,10):
			time.sleep(.1)
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				returned = None
				return
		
		
	elif num == 1:
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,000))
		led.show()
		for i in range(0,5):
			time.sleep(.1)
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				returned = None
				return	
		
		
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,255))
		led.show()
		for i in range(0,5):
			time.sleep(.1)
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				returned = None
				return
		
		
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,000))
		led.show()
		for i in range(0,5):
			time.sleep(.1)
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				returned = None
				return
		
		
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,255))
		led.show()
		for i in range(0,5):
			time.sleep(.1)
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				returned = None
				return
		
		
		for j in range(0, leds):
			led.setPixelColor(j, Color(0,0,000))
		led.show()
		for i in range(0,10):
			time.sleep(.1)
			if GPIO.input(10) == GPIO.HIGH:
				print("Button was pushed! ")	
				btnPress = True
				returned = None
				return

"""cycle
Cycle through all available options
Parameter1- number of animation/color in cycle that is selected
"""
def cycle(num = 0):
	global btnPress
	global returned
	global mode
	mode = num
	sleep = False
	limit = 20
	while True:
		
		print("mode "+str(mode))
		sleep = checkBtnPressed(limit, True)
			
		if mode == -1:
			setColorW(60, "CLEAR")
		if mode == 0:
			setColorW(60,"RED")
		if mode == 1:
			setColorW(60, "PINK")
		if mode == 2:
			setColor(60, (162,0,255))
		if mode == 3:
			setColorW(60,"BLUE")
		if mode == 4:
			setColor(60, (0,162,255))
		if mode == 5:
			setColor(60, (0,255,252))
		if mode == 6:
			setColor(60, (0,255,102))
		if mode == 7:
			setColor(60, (68,255,0))
		if mode == 8:
			setColor(60, (230,255,0))
		if mode == 9:
			setColor(60, (255,188,0))
		if mode == 10:
			setColor(60, (255,112,0))
		if mode == 11:
			setColorW(60, "WHITE")
		if mode == 12:
			setColorW(60, "WARM")
		if mode == 13:
			setColor(60, (230,255,0))
		if mode == 14:
			breathe(60)
			wasBtnPressed()
			
			
		if mode == 15:
			if returned == None:
				wave(60)
			else:
				print(returned)
				wave(60, returned)
			wasBtnPressed()
			
			
		if mode == 16:
			if returned == None:
				changing(60)
			else:
				print(returned)
				changing(60, returned)

			wasBtnPressed()
		
		if mode == 17:
			if returned == None:
				breathe3(60)
			else:
				print(returned)
				breathe3(60, returned)

			wasBtnPressed()
				
		if mode ==18:
			if returned == None:
				shiftSolid(60)
			else:
				print(returned)
				shiftSolid(60, returned)
				
			wasBtnPressed()
			
			
		if mode == 19:
			notify(60, 1)
			wasBtnPressed()

		num = getNumberRequest(num)
			




"""checkBtnPressed
checks if the gpio button was pressed
If so global varaible mode is increased
"""			
def checkBtnPressed(limit = 20, simple = False):
	global btnPress
	global returned
	global mode
	global httpChange

	
	if GPIO.input(10) == GPIO.HIGH:
		startTime = time.time()
		while GPIO.input(10) == GPIO.HIGH:
			holdTime = time.time()-startTime
			if(holdTime > 2):
				print("TURNING OFF")
				#mode = -2
				turnOff()
				break
			#pass
		holdTime = time.time()-startTime
		print("HELD FOR END TIME: "+str(holdTime))
		if(holdTime > 2):
			print("TURNING OFF")
			mode = -2
		print("Button was pushed! "+str(mode))	
		mode += 1
		if mode == limit:
			mode = -1
		returned = None
		if simple == False:
			btnPress = True
		time.sleep(.25)
		return True
	return False

"""checkBtnPressed2
checks if the btnPress global variable was pressed.
If so global varaible mode is increased
"""
def	wasBtnPressed(limit = 20):
	global btnPress
	global returned
	global mode
	global httpChange
	
	if(btnPress):
		print("button press = true")
		mode += 1
		if mode == limit:
			mode = 0
		btnPress = False
		returned = None	
		time.sleep(.25)
		return True
		
	return False

"""getNumberRequest
sends http request to web server to check if mode was increased remotely
Parameter1- the value of mode before the http request check
"""		
def getNumberRequest(old):
	global url
	global returned
	global mode
	global httpChange
	global enc
	global firstConnect
	
	if(enc < 5):
		try:
			r = requests.get(url)
			num = int(r.text)
			#enc = 0
			#s = request.get(url+"/settings")
			#print(s.text)		
		except:
			try:
				print("Error: http connection failed trying again")
				time.sleep(.01)
				r = requests.get(url)
				#s = request.get(url+"/settings")
				#print(s.text)
				num = int(r.text)
			except:
				print("Error: http connection failed again. http request not available")
				num = old
				print(firstConnect)
				if(firstConnect == False):
					enc+=1
				enc+=1
				print("enc "+str(enc))
			
		if(num != old):
			enc = 0
			returned = None
			mode = num
			return mode
		
		if(num == old and firstConnect == True):
			print("apple")
			firstConnect = False
			print(firstConnect)
			enc = 0
			returned = None
			mode = num
			return mode
	
	return old

def checkNumberRequest(old):
	global url
	global returned
	global mode
	global httpChange
	global enc
	
	if(enc < 10):
		try:
			r = requests.get(url)
			num = int(r.text)		
		except:
			try:
				print("Error: http connection failed trying again")
				time.sleep(.01)
				r = requests.get(url)
				num = int(r.text)
			except:
				print("Error: http connection failed again. http request not available")
				num = old
				enc+=1
		if(num != old):
			return True
	
	return False

"""turnOff
turnes off leds and exits the script

"""
def turnOff():
	setColorW(60,"CLEAR")
	time.sleep(.5)
	#subprocess.call("sudo poweroff", shell=True) #Shuts down rpi
	#exit() #closes script



if __name__ == "__main__":
    cycle()		

