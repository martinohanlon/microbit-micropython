import mcpi.minecraft as minecraft
import mcpi.block as block
import minecraftstuff as mcstuff
import math
from threading import Thread
from time import sleep

# finds point on sphere (based on polar co-ordinates) 
def findPointOnSphere(cx, cy, cz, radius, phi, theta):
    #phi - angle around the pole 0<= phi <= 360
    #theta - angle from plan 'up' -90 <= theta <= 90
    x = cx + radius * math.cos(math.radians(theta)) * math.cos(math.radians(phi))
    z = cz + radius * math.cos(math.radians(theta)) * math.sin(math.radians(phi))
    y = cy + radius * math.sin(math.radians(theta))
    return int(round(x,0)), int(round(y,0)), int(round(z,0))

class StarwarsCraft:
    def __init__(self, craftBlocks, pos):

        self.mc = minecraft.Minecraft.create()

        #create the craft
        self.craftShape = mcstuff.MinecraftShape(self.mc, pos, craftBlocks)

        self.flying = False
        self.turnYawAngle = 0
        self.pitchAngle = 0

    #fly the craft to a position, speed is the time to wait between moving
    def flyTo(self,x,y,z,speed,background=False):
        #run it in its own thread
        flyToThread = Thread(None, self._flyTo, None, (x, y, z, speed))
        flyToThread.start()
        
        #if backgroud == True, return the thread, otherwise wait for it to finish
        if background == False:
            flyToThread.join()

        return flyToThread

    def _flyTo(self,x,y,z,speed):
        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        blocksBetween = mcDraw.getLine(self.craftShape.position.x,
                                       self.craftShape.position.y,
                                       self.craftShape.position.z,
                                       x,
                                       y,
                                       z)
        
        for blockBetween in blocksBetween:
            self.craftShape.move(blockBetween.x, blockBetween.y, blockBetween.z)
            # time to sleep between each block move
            sleep(speed)

    def fly(self, speed):
        self.flying = True
        self.flyThread = Thread(None, self._fly, None, (speed,))
        self.flyThread.start()
        
        return self.flyThread

    def _fly(self, speed):
        while self.flying:
            if self.turnYawAngle != 0:
                self.rotateBy(self.turnYawAngle, 0, 0)
            
            x, y, z = findPointOnSphere(self.position.x, self.position.y, self.position.z,
                                        1, self.craftShape.yaw - 90, self.craftShape.pitch)
            self.craftShape.move(x,y,z)
            sleep(speed)

    def stop(self):
        self.flying = False
        self.flyThread.join()

    def clear(self):
        self.craftShape.clear()
    
    def draw(self):
        self.craftShape.draw()

    def rotate(self, yaw, pitch, roll):
        self.craftShape.rotate(yaw, pitch, roll)

    def rotateBy(self, yaw, pitch, roll):
        self.craftShape.rotateBy(yaw, pitch, roll)

    def turn(self, angle):
        self.turnYawAngle = angle

    @property
    def position(self):
        return self.craftShape.position

class TieFighter(StarwarsCraft):
    def __init__(self, pos):
        
        #create the tie fighter
        tieBlocks = [mcstuff.ShapeBlock(0,0,0,block.IRON_BLOCK),
                     mcstuff.ShapeBlock(-1,-1,-1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(-1,-1,0,block.WOOL.id,15),
                     mcstuff.ShapeBlock(-1,-1,1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(-1,0,-1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(-1,0,0,block.WOOL.id,15),
                     mcstuff.ShapeBlock(-1,0,1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(-1,1,-1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(-1,1,0,block.WOOL.id,15),
                     mcstuff.ShapeBlock(-1,1,1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,-1,-1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,-1,0,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,-1,1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,0,-1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,0,0,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,0,1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,1,-1,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,1,0,block.WOOL.id,15),
                     mcstuff.ShapeBlock(1,1,1,block.WOOL.id,15),
                     ]
        
        #instantiate the tie fighter
        StarwarsCraft.__init__(self, tieBlocks, pos)

class MilleniumFalcon(StarwarsCraft):
    def __init__(self, pos):
        
        #create the millenium falcon
        falconBlocks = [mcstuff.ShapeBlock(-1,0,-2,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(0,0,-2,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(1,0,-2,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-2,0,-1,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-1,0,-1,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(0,1,-1,block.WOOL.id,8),
                        mcstuff.ShapeBlock(1,0,-1,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(2,0,-1,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-3,0,0,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-2,0,0,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-1,1,0,block.WOOL.id,8),
                        mcstuff.ShapeBlock(0,1,0,block.WOOL.id,8),
                        mcstuff.ShapeBlock(1,1,0,block.WOOL.id,8),
                        mcstuff.ShapeBlock(2,0,0,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(3,0,0,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-3,0,1,block.WOOL.id,7),
                        mcstuff.ShapeBlock(-2,0,1,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-1,0,1,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(0,1,1,block.WOOL.id,8),
                        mcstuff.ShapeBlock(1,0,1,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(2,0,1,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-3,0,2,block.WOOL.id,7),
                        mcstuff.ShapeBlock(-1,0,2,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(0,0,2,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(1,0,2,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-1,0,3,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(1,0,3,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(-1,0,4,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(1,0,4,block.IRON_BLOCK),
                        mcstuff.ShapeBlock(0,0,-1,block.WOOL.id,8),
                        mcstuff.ShapeBlock(-1,0,0,block.WOOL.id,8),
                        mcstuff.ShapeBlock(0,0,0,block.WOOL.id,8),
                        mcstuff.ShapeBlock(1,0,0,block.WOOL.id,8),
                        mcstuff.ShapeBlock(0,0,1,block.WOOL.id,8)
                        ]

        
        #instantiate the falcon
        StarwarsCraft.__init__(self, falconBlocks, pos)

class XWingFighterDiagonal(StarwarsCraft):
    def __init__(self, pos):
        #create the x wing
        xWingBlocks = [mcstuff.ShapeBlock(-2,1,-2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(2,0,-2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-3,1,-1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(1,0,-1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-3,1,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-2,1,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-1,1,0,block.WOOL.id, 8),
                       mcstuff.ShapeBlock(0,0,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-2,1,1,block.WOOL.id, 8),
                       mcstuff.ShapeBlock(-1,1,1,block.WOOL.id, 3),
                       mcstuff.ShapeBlock(0,1,1,block.WOOL.id, 8),
                       mcstuff.ShapeBlock(-1,1,2,block.WOOL.id, 8),
                       mcstuff.ShapeBlock(0,1,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(2,1,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(0,1,3,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(1,1,3,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-2,-1,-2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-3,-1,-1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-3,-1,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-2,0,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-1,0,0,block.WOOL.id, 8),
                       mcstuff.ShapeBlock(-2,0,1,block.WOOL.id, 8),
                       mcstuff.ShapeBlock(-1,0,1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(0,0,1,block.WOOL.id, 8),
                       mcstuff.ShapeBlock(-1,0,2,block.WOOL.id, 8),
                       mcstuff.ShapeBlock(0,0,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(2,-1,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(0,-1,3,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(1,-1,3,block.IRON_BLOCK)]
                       
        #instantiate the x wing
        StarwarsCraft.__init__(self, xWingBlocks, pos)


class XWingFighter(StarwarsCraft):
    def __init__(self, pos):
        #create the x wing
        xWingBlocks = [mcstuff.ShapeBlock(0,0,-2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(0,0,-1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(0,0,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-3,1,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(0,0,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(3,1,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-3,1,1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-1,1,1,block.WOOL.id,8),
                       mcstuff.ShapeBlock(0,1,1,block.WOOL.id,3),
                       mcstuff.ShapeBlock(1,1,1,block.WOOL.id,8),
                       mcstuff.ShapeBlock(3,1,1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-2,1,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-1,1,2,block.WOOL.id,8),
                       mcstuff.ShapeBlock(0,1,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(1,1,2,block.WOOL.id,8),
                       mcstuff.ShapeBlock(2,1,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-3,-1,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(3,-1,0,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-3,-1,1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-1,0,1,block.WOOL.id,8),
                       mcstuff.ShapeBlock(0,0,1,block.WOOL.id,3),
                       mcstuff.ShapeBlock(1,0,1,block.WOOL.id,8),
                       mcstuff.ShapeBlock(3,-1,1,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-2,-1,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(-1,0,2,block.WOOL.id,8),
                       mcstuff.ShapeBlock(0,0,2,block.IRON_BLOCK),
                       mcstuff.ShapeBlock(1,0,2,block.WOOL.id,8),
                       mcstuff.ShapeBlock(2,-1,2,block.IRON_BLOCK)] 
                       
        #instantiate the x wing
        StarwarsCraft.__init__(self, xWingBlocks, pos)


#tests
if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    
    playerPos = mc.player.getTilePos()
    craftPos = playerPos.clone()
    craftPos.y += 10
    craftPos.z += 20
    craft = XWingFighter(craftPos)
    sleep(5)

    craft.fly(0.25)
    sleep(5)
    craft.turn(5)
    sleep(10)
    craft.turn(-5)
    sleep(10)
    craft.turn(0)
    sleep(5)
    craft.stop()
    sleep(2)
    craft.clear()

if __name__ == "old__main__":

    mc = minecraft.Minecraft.create()
    
    playerPos = mc.player.getTilePos()


    #create the craft around the player
    tie1Pos = playerPos.clone()
    tie1Pos.x -= 10
    tie1 = TieFighter(tie1Pos)

    tie2Pos = playerPos.clone()
    tie2Pos.x += 10
    tie2 = TieFighter(tie2Pos)
    falconPos = playerPos.clone()
    falconPos.z += 10
    falcon = MilleniumFalcon(falconPos)
    xWingPos = playerPos.clone()
    xWingPos.y += 10
    xWing = XWingFighter(xWingPos)

    sleep(25)

    #set the craft to fly (threaded)
    tie1Fly = tie1.fly(tie1Pos.x, tie1Pos.y, tie1Pos.z + 25, 0.25, True)
    tie2Fly = tie2.fly(tie2Pos.x, tie2Pos.y, tie2Pos.z + 25, 0.25, True)
    falconFly = falcon.fly(falconPos.x, falconPos.y, falconPos.z + 25, 0.25, True)
    xWingFly = xWing.fly(xWingPos.x + 25, xWingPos.y, xWingPos.z - 25, 0.25, True)

    #wait for the craft to stop
    tie1Fly.join()
    tie2Fly.join()
    falconFly.join()
    xWingFly.join()

    #clear the craft
    tie1.clear()
    tie2.clear()
    falcon.clear()
    xWing.clear()
