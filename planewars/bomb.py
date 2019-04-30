
import pyxel as px



__doc__="""
爆炸效果

"""


class Bomb():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.isdel = False
        self.bombAnim = 0

    def drawBomb(self):
        px.blt(self.x,self.y,2,self.bombAnim,0,16,16,0)


    def updateBomb(self):
        if px.frame_count % 1 == 0:
        # print("转向",self.player.playerAnim)
            self.bombAnim += 16
            if self.bombAnim >= 16*9:
                self.isdel = True
            