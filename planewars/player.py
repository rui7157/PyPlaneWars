import pyxel as px

__doc__ ="""
玩家

"""

class Player():

    def __init__(self):
        self.playerX = px.width/2-8
        self.playerY = px.height-16
        self.playerAnim = 16


