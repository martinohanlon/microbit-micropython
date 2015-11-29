import microbit

TOLERANCE = 3000
MESSAGES = ["It is certain", "Dont count on it", "Ask again"]

def get_accel_total():
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()
    return x + y + z

def wait_for_shake():
    shaken = False
    last = get_accel_total()
    while not shaken:
        this = get_accel_total()
        diff = last - this
        if diff < 0: diff = diff * -1
        if diff > TOLERANCE:
            shaken = True
        last = this
        microbit.sleep(50)

while True:
    microbit.display.print("8")
    wait_for_shake()
    microbit.display.clear()
    microbit.sleep(2000)
    message = microbit.random(len(MESSAGES))
    microbit.display.scroll(MESSAGES[message])
