from microbit import *
import music

# The theme tune to a certain film franchise. Connect a speaker to pin0 and GND. The force is strong with this... ;-)
tune = ('c4:6', 'g:3', 'f:1', 'e', 'd', 'c5:6', 'g4:3', 'f:1', 'e', 'd', 'c5:6', 'g4:3', 'f:1', 'e', 'f', 'd:6', 'r:6')

REFRESH = 500

def get_data():
    x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
    a, b = button_a.was_pressed(), button_b.was_pressed()
    print(x, y, z, a, b)

def run():
	while True:
		sleep(REFRESH)
		get_data()

display.show('M')
# Play the theme tune, don't block and keep looping. Gets quite annoying after a while... ;-)
music.play(theme, wait=False, loop=True)
run()
music.stop()
