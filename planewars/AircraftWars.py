import pyxel as px
import glfw
import random


__doc__ = """
飞机大战游戏

动画更新频率可以做成装饰器或者专门的函数实现



"""


class App:
    def __init__(self):
        px.init(123, 200, scale=0)
        px.load("AircraftWars.pyxel")
        #调试信息
        self.dprint = ""

        self.score=0
        self.playerX = px.width/2-8
        self.playerY = px.height-16
        self.playerAnim = 16
        self.lrKey = ""
        self.playerLeftToRight = 16
        self.playerUpToDown = 16
        self.initBullet()
        self.initBG()
        self.initEnemy()
        px.mouse = True
        px.run_with_profiler(self.update, self.draw)

    def playerInput(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btn(px.KEY_LEFT) or px.btn(px.GAMEPAD_1_LEFT):
            self.playerX = max(self.playerX - 2, 0)

        if px.btn(px.KEY_RIGHT) or px.btn(px.GAMEPAD_1_RIGHT):
            self.playerX = min(self.playerX + 2, px.width - 16)
            # self.lrKey = "right"
        if px.btn(px.KEY_UP) or px.btn(px.GAMEPAD_1_LEFT):
            self.playerY = max(self.playerY - 2, 0)

        if px.btn(px.KEY_DOWN) or px.btn(px.GAMEPAD_1_RIGHT):
            self.playerY = min(self.playerY + 2, px.height - 16)

        if px.btnp(px.KEY_LEFT):
            self.lrKey = "left"
            self.playerAnim = 64
            self.playerLeftToRight = 16
            # print("press LEFT")
            self.dprint = "press LEFT"

        if px.btnp(px.KEY_RIGHT):
            self.lrKey = "right"
            self.playerLeftToRight = -16
            self.playerAnim = 64
            # print("press RIGHT")
            self.dprint = "press RIGHT"

        if px.btnr(px.KEY_LEFT) or px.btnr(px.KEY_RIGHT):
            self.lrKey = ""

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
        objAnimValue = getattr(self, objName)
        if px.frame_count % pl == 0:
            objAnimValue += width
            setattr(self, objName, objAnimValue)
            if objAnimValue >= firstGrid+width*anmCount:
                # objAnimValue=firstGrid
                setattr(self, objName, firstGrid+width*(anmCount-1))

    def updateAirAnimate(self, dire=""):
        #飞机动画

        if dire == "left":
            self.disposableAnim("playerAnim", 64, 16, 2, 10)
        elif dire == "right":
            self.disposableAnim("playerAnim", 64, 16, 2, 10)
        else:
            self._updateAnimate("playerAnim", 0, 16, 4)

    def initBullet(self):
        self.bX = self.playerX+8
        self.bY = self.playerY-8
        self.bR = 1

    def displayBullet(self):
        #初始化子弹
        px.circ(self.bX, self.bY, self.bR, 7)

    def updateBullet(self):
        #更新子弹
        # self.bullet =
        self.bY -= 10
        if self.bY <= 0:
            self.bY = self.playerY
            self.bX = self.playerX+8

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


#敌人

    def initEnemy(self):
        self.eX = random.randint(2, px.width-2)
        self.eY = 2
        self.lv = random.randint(2, 8)
        self.clr = random.randint(1, 16)

    def displayEnemy(self):
        px.circ(self.eX, self.eY, self.lv, self.clr)

    def updateEnemy(self):
        #敌人移动轨迹
        if px.frame_count % 4 == 0:
            self.eY += 5

            lrmove = random.randint(0, 10)
            if lrmove < 3:
                self.eX -= 4
            elif lrmove > 6:
                self.eX += 4
        if self.eX > px.height-4:
            self.eX = px.height - 4
        elif self.eX < 4:
            self.eX = 4

        if self.eY > px.height:
            self.initEnemy()
            self.eY = 0

    def checkHit(self,x1, y1, r1, x2, y2, r2) -> bool:
        """命中检测"""
        hit = False
        
        # print((x1-x2)*2+(y1-y2)*2)
        if(x1-x2)**2+(y1-y2)**2<=(r1+r2)**2:
            print(x1, y1, r1, x2, y2, r2)
            print((x1-x2)**2+(y1-y2)**2)
            print((r1+r2)**2)
            hit = True
        return hit

    def bulletHitEnemy(self):
        #子弹命中敌人
        if self.checkHit(self.bX, self.bY, self.bR+1, self.eX, self.eY, self.lv):
            #已经命中
            self.initBullet()
            self.initEnemy()
            self.score+=1

    def update(self):
        #每帧更新
        self.playerInput()
        self.updateBullet()
        self.updateEnemy()
        #动画区域firstGrid-endGrid
        self.updateAirAnimate(self.lrKey)
        self.updateBG()
        self.bulletHitEnemy()
        self.dprint = "->{}".format(px.frame_count)

    def draw(self):
        #绘图
        px.cls(0)
        px.blt(
            self.playerX,
            self.playerY,
            0,
            self.playerAnim,
            0,
            self.playerLeftToRight,
            self.playerUpToDown,
            12
        )

        # print(self.playerLeftToRight)
        #背景
        self.displayBG()
        #子弹
        self.displayBullet()
        #敌人
        self.displayEnemy()

        # px.text(5,4,"this a game deme ",7)
        px.text(0, 4, "Debug:{}".format(self.dprint), 7)
        px.text(0, 10, "Score:{}".format(self.score), 7)

if __name__ == "__main__":
    App()
