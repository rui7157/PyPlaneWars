import pyxel as px
import glfw
import random
from enemy import Enemy
from player import Player 
__doc__ = """
飞机大战游戏

动画更新频率可以做成装饰器或者专门的函数实现



"""

class TestPlayer():
    pX = 60

class App:
    def __init__(self):
        px.init(123, 200, scale=0)
        px.load("AircraftWars.pyxel")
        #调试信息
        self.dprint = ""

        self.score=0
        self.player = Player()

        self.playerAnim = 16
        self.lrKey = ""
        self.initBullet()
        self.initBG()
        self.initNewEnemy()
        # self.initEnemy()
        px.mouse = True
        px.run_with_profiler(self.update, self.draw)

    def playerInput(self):

        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btn(px.KEY_LEFT) or px.btn(px.GAMEPAD_1_LEFT):
            self.player.x = max(self.player.x - 2, 0)

        if px.btn(px.KEY_RIGHT) or px.btn(px.GAMEPAD_1_RIGHT):
            self.player.x = min(self.player.x + 2, px.width - 16)

        if px.btn(px.KEY_UP) or px.btn(px.GAMEPAD_1_LEFT):
            self.player.y = max(self.player.y - 2, 0)

        if px.btn(px.KEY_DOWN) or px.btn(px.GAMEPAD_1_RIGHT):
            self.player.y = min(self.player.y + 2, px.height - 16)



        if px.btnp(px.KEY_LEFT):
            self.lrKey = "left"
            self.player.playerAnim = 64
            self.player.playerLeftToRight = 16
            # print("press LEFT")
            self.disposableAnim("playerAnim", 64, 16, 2, 10)
            self.dprint = "press LEFT"

        if px.btnp(px.KEY_RIGHT):
            self.lrKey = "right"
            self.player.playerLeftToRight = -16
            self.player.playerAnim = 64
            # print("press RIGHT")
            self.disposableAnim("playerAnim", 64, 16, 2, 10)
            self.dprint = "press RIGHT"

        if px.btnr(px.KEY_LEFT) or px.btnr(px.KEY_RIGHT):
            self._updateAnimate("playerAnim", 0, 16, 4)
        self._updateAnimate("playerAnim", 0, 16, 4)

    def _updateAnimate(self, objName: str, firstGrid, width, anmCount, pl=4):
        """循环播放"""
        #对象名字(self.playerAnim),起始X坐标,图片宽度,图片数量,动画频率
        objAnimValue = getattr(self, objName)
        # objAnim = 200
        # print(self.playerAnim)
        if px.frame_count % pl == 0:
            objAnimValue += width
            setattr(self, objName, objAnimValue)
            if objAnimValue >= firstGrid+width*anmCount:
                objAnimValue = firstGrid
                setattr(self, objName, objAnimValue)
        # print(getattr(self,objName))


    def disposableAnim(self, objName: str, firstGrid, width, anmCount, pl=2):
        #一次性动画
        # setattr(self,objName,firstGrid)
        objAnimValue = getattr(self.player, objName)
        if px.frame_count % pl == 0:
            objAnimValue += width
            setattr(self.player, objName, objAnimValue)
            if objAnimValue >= firstGrid+width*anmCount:
                # objAnimValue=firstGrid
                setattr(self.player, objName, firstGrid+width*(anmCount-1))

    

    # def updateAirAnimate(self, dire=""):
    #     #飞机动画

    #     if dire == "left":
    #         self.disposableAnim("playerAnim", 64, 16, 2, 10)
    #     elif dire == "right":
    #         self.disposableAnim("playerAnim", 64, 16, 2, 10)
    #     else:
    #         self._updateAnimate("playerAnim", 0, 16, 4)

    def initBullet(self):
        self.bX = self.player.x+8
        self.bY = self.player.y-8
        self.bR = 1

    def displayBullet(self):
        #初始化子弹
        px.circ(self.bX, self.bY, self.bR, 7)

    def updateBullet(self):
        #更新子弹
        # self.bullet =
        self.bY -= 10
        if self.bY <= 0:
            self.bY = self.player.y
            self.bX = self.player.x+8

    def initBG(self):
        #初始化背景
        self.bgx = 0
        self.bgy = 0

    def displayBG(self):
        bgWidth = 1
        bgHeight = 8
        #背景左边
        px.rect(self.bgx, self.bgy, self.bgx+bgWidth-1, self.bgy+bgHeight, 6)
        #背景右边
        px.rect(self.bgx+px.width-1, self.bgy, self.bgx +
                px.width+bgWidth-1, self.bgy+bgHeight, 6)

    def updateBG(self):
        self.bgy += 16
        if self.bgy >= px.height:
            self.bgy = 0





    def checkHit(self,x1, y1, r1, x2, y2, r2) -> bool:
        """命中检测"""
        hit = False
        
        if(x1-x2)**2+(y1-y2)**2<=(r1+r2)**2:
            hit = True
        return hit

    def bulletHitEnemy(self):
        #子弹命中敌人
        if hasattr(self,"enemy"):
            if self.checkHit(self.bX, self.bY, self.bR+1, self.enemy.x, self.enemy.y, 8):
                #已经命中
                self.initBullet()
                
                del self.enemy
                self.initNewEnemy()
                # self.initEnemy()
                self.score+=1

    def initNewEnemy(self):
        self.enemy = Enemy(self.player,moveMode=random.randint(1,6))


    def animate(self,obj,animeDirection=0):
        """制作动画
        跳帧方向，默认从左到右
        0从左到右
        1从右到左
        2从上到下
        3从下到上
        """
        pass





    def update(self):
        #每帧更新
        self.playerInput()
        self.updateBullet()
        if hasattr(self,"enemy"):
            self.enemy.updateEnemy()
            self.bulletHitEnemy()
            
            if self.enemy.isdel:
                del self.enemy
                self.initNewEnemy()
            
        #动画区域firstGrid-endGrid
        # self.updateAirAnimate(self.lrKey)
        self.updateBG()
        self.dprint = "->{}".format(px.frame_count)

    def draw(self):

        
        #绘图
        px.cls(0)
        self.player.drawPlayer()
        #背景
        self.displayBG()
        #子弹
        self.displayBullet()
        
        if hasattr(self,"enemy") and self.enemy != None:
            self.enemy.drawEnemy()
        # px.text(5,4,"this a game deme ",7)
            px.text(0, 4, "Debug:{}".format(str(int(self.enemy.y))+":"+str(self.enemy.x)),7)
        px.text(0, 10, "Score:{}".format(self.score), 7)

if __name__ == "__main__":
    App()
