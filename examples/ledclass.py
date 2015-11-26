import microbit

class LED():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def on(self, brightness = 9):
        microbit.display.set_pixel(self.x, self.y, brightness)

    def off(self):
        microbit.display.set_pixel(self.x, self.y, 0)

led = LED(2,2)

while True:
    led.on()
    microbit.sleep(500)
    led.off()
    microbit.sleep(500)
    
