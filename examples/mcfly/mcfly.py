import serial
from starwarscraft import XWingFighter
from bomb import Bomb
from mcpi.minecraft import Minecraft
from time import sleep

PORT = "COM3"
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
#read the first line and flush any bad data
s.readline()


def read_microbit_data():
    #read a line from the microbit, 
    data = s.readline()
    #split the microbit data into x, y, z, a, b
    data_s = data.rstrip().split(" ")
    x, y, z = int(data_s[0]), int(data_s[1]), int(data_s[2])
    a = True if data_s[3] == "True" else False
    b = True if data_s[4] == "True" else False
    #debug
    #print(x, y, z)
    #print(a, b)
    return x, y, z, a, b

mc = Minecraft.create()

try:
    playerPos = mc.player.getTilePos()
    craftPos = playerPos.clone()
    craftPos.y += 10
    craftPos.z += 20
    craft = XWingFighter(craftPos)
    bomb = Bomb()
    
    while True:
        x, y, z, a, b = read_microbit_data()
        if a:
            if craft.flying:
                craft.stop()
            else:
                craft.fly(0.15)
        if b:
            bpos = craft.craftShape.position
            bpos.y - 2
            bomb.drop(bpos.x, bpos.y, bpos.z, 0.1)
        if x > 750:
            craft.turn(10)
        if x > 500:
            craft.turn(5)
        if x < -750:
            craft.turn(-10)
        if x < -500:
            craft.turn(-5)
        if x > -500 and x < 500:
            craft.turn(0)
    
finally:
    sleep(1)
    craft.clear()
    s.close()
