from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
from mcpi import block
from time import sleep
from threading import Thread

class Bomb:
    def __init__(self, blast = 5):

        self.mc = Minecraft.create()
        self.blast = blast

    def drop(self, x, y, z, speed, background=False):
        #run it in its own thread
        dropThread = Thread(None, self._drop, None, (x, y, z, speed))
        dropThread.start()
        
        #if backgroud == True, return the thread, otherwise wait for it to finish
        if background == False:
            dropThread.join()

        return dropThread

    def _drop(self, x, y, z, speed):
        exploded = False
        while not exploded:
            self.mc.setBlock(x, y, z, block.TNT.id)
            sleep(speed)
            self.mc.setBlock(x, y, z, block.AIR.id)
            y = y - 1
            if self.mc.getBlock(x, y, z) != block.AIR.id:
                exploded = True
                self.mc.postToChat("boom")
                mcdraw = MinecraftDrawing(self.mc)
                mcdraw.drawSphere(x, y, z, self.blast, block.AIR.id)
            
