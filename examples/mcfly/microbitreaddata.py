from microbit import *

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
run()
