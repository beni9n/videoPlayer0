# videoPlayer0
## Button Mapping:
	You will  likely want to remap buttons based on your needs. In order to do so you need to.
	`button_loop = 22`</br>
	`button_pause = 17`</br>
	`button_next = 18`</br>
	`button_previous = 4`</br>
	`button_restart = 21`</br>
 A video player for the Raspberry Pi with GPIO controls. Scripted in Python. 
 ##Requirements:
 VLC Configured to accept telnet connections:
 `vlc -I telnet --telnet-password test`
 You will need to have a playlist and pass it as a parameter to the vlc command above.
