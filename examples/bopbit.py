from microbit import *

#constants
# the speed is based on level, the higher the level, the faster the speed
SPEED = {0: 1000, 1: 750, 2: 650, 3: 600, 4: 550, 5: 500}
# you level up when you score these points
LEVELUP = (5, 10, 15, 20, 25, 30)

def show_a():
    display.clear()
    display.show("A")

def show_b():
    display.clear()
    display.show("B")

def show_tick():
    display.clear()
    display.set_pixel(0, 3, 9)
    display.set_pixel(1, 4, 9)
    display.set_pixel(2, 3, 9)
    display.set_pixel(3, 2, 9)
    display.set_pixel(4, 1, 9)
    
def show_cross():
    display.clear()
    display.show("X")

def wait_for_button(rightbutton, wrongbutton):
    rightpressed = False
    wrongpressed = False
    
    started = running_time()
    now = running_time()
    
    while now - started < SPEED[level]:
        if rightbutton.is_pressed():
            rightpressed = True
        if wrongbutton.is_pressed():
            wrongpressed = True
        now = running_time()
        
    if rightpressed == True and wrongpressed == False:
        return True
    else:
        return False

#set the score
level = 0
score = 0
gameover = False

display.scroll("BopBit")

#loop until game over
while gameover == False:

    success = False
    
    #randomly pick an A or B button
    action = random(2)
    
    #wait for the button to be pressed
    if action == 0:
        show_a()
        success = wait_for_button(button_a, button_b)
    elif action == 1:
        show_b()
        success = wait_for_button(button_b, button_a)
    
    #did the player get to the right button
    if success:
        show_tick()
        score = score + 1
        #if the score is a levelup score increase the level 
        if score in LEVELUP:
            level = level + 1
    else:
        show_cross()
        gameover = True

    sleep(int(SPEED[level] / 2))
    
#game over - show the players score on a loop
sleep(1000)
while True:
    display.scroll("{} points".format(score))
    