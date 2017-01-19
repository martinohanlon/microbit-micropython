import microbit

TOLERANCE = 3000
MESSAGES = ["It is certain", "Dont count on it", "Ask again""It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely". "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

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
