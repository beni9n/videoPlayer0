import RPi.GPIO as GPIO
import time
import telnetlib

# button mapping:
button_loop = 22
button_pause = 17
button_next = 18
button_previous = 4
button_restart = 21

# configure GPIO buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_loop, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_pause, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_next, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_previous, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_restart, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#configure telnet
hostserver = "127.0.0.1"
hostport = "4212"
newline = "\n"
password = "test"

# estable telnet connection for use
telnet = telnetlib.Telnet(hostserver, hostport)
telnet.read_until("Password: ")
telnet.write(password + newline)
telnet.read_until("> ")

while True:
	# play previous item
	if(GPIO.input(button_previous)==1):
		print("Previous button was pressed")
		telnet.write("prev " + newline)
		time.sleep(1)
	
	# next track please
	if(GPIO.input(button_next)==1):
		print("Next button was pressed")
		telnet.write("next " + newline)
		time.sleep(1)
	
	# pause / play		
	if(GPIO.input(button_pause)==1):
		print("Pause button was pressed")
		telnet.write("pause " + newline)	
		time.sleep(1)
	
	# restart the current track
	if(GPIO.input(button_restart)==1):
		print("Restart button pressed")
		telnet.write("seek 0 " + newline)
		time.sleep(1)

	# loop the playlist
	if(GPIO.input(button_loop)==1):
		print("Loop button was pressed")
		telnet.write("loop " + newline)
		time.sleep(1)
GPIO.cleanup()
