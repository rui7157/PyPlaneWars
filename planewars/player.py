import pyxel as px

__doc__ ="""
玩家

"""

class Player():

    def __init__(self):
        self.x = px.width/2-8
        self.y = px.height-16
        self.playerAnim = 16
        self.playerLeftToRight = 16
        self.playerUpToDown = 16



    def updatePlayer(self):
        pass

    

    def drawPlayer(self):
        px.blt(
            self.x,
            self.y,
            0,
            self.playerAnim,
            0,
            self.playerLeftToRight,
            self.playerUpToDown,
            12
        )