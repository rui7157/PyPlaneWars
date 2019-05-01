import pyxel as px
import glfw
import random
from enemy import Enemy
from player import Player 
from bomb import Bomb
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
        self.gameover = False
        self.score=0
        self.player = Player()
        self.playerAnimateStatus = "run"
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
            self.turnPosAnimate("left")
        if px.btn(px.KEY_RIGHT) or px.btn(px.GAMEPAD_1_RIGHT):
            self.player.x = min(self.player.x + 2, px.width - 16)
            self.turnPosAnimate("right")
            
        if px.btn(px.KEY_UP) or px.btn(px.GAMEPAD_1_LEFT):
            self.player.y = max(self.player.y - 2, 0)

        if px.btn(px.KEY_DOWN) or px.btn(px.GAMEPAD_1_RIGHT):
            self.player.y = min(self.player.y + 2, px.height - 16)


        if px.btnr(px.KEY_LEFT) or px.btnr(px.KEY_RIGHT):
            self.playerAnimateStatus= "run"

        self.updatePlayerAnimate()


    def updatePlayerAnimate(self):
        """循环播放"""
        if self.playerAnimateStatus == "stop":
            return 
        if px.frame_count % 4 == 0:
            self.player.playerAnim += 16
            if self.player.playerAnim >= 0+16*4:
                self.player.playerAnim = 0

    def turnPosAnimate(self,dir:str):
        """制作动画转向
        """
        self.playerAnimateStatus = "stop"

        if dir =="left":
            self.player.playerLeftToRight = 16
        elif dir == "right":
            self.player.playerLeftToRight = -16

        if self.player.playerAnim<16*4:
            self.player.playerAnim = 16*4

        if px.frame_count % 8 == 0:
            if self.player.playerAnim >= 16*3+16*3:
                self.player.playerAnim = 16*3+16*3
            else:
                self.player.playerAnim += 16

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
            if self.checkHit(self.bX, self.bY, self.bR+1, self.enemy.x+8, self.enemy.y+8, 8):
                #已经命中
                self.initBullet()
                self.bomb = Bomb(self.enemy.x,self.enemy.y)
                del self.enemy
                self.initNewEnemy()
                # self.initEnemy()
                self.score+=1
            if self.checkHit(self.player.x+8, self.player.y+8, 4, self.enemy.x+8, self.enemy.y+8, 8):
                self.bomb = Bomb(self.player.x,self.player.y)
                self.gameover=True
            

    def initNewEnemy(self):
        self.enemy = Enemy(self.player,moveMode=random.randint(1,6))

    def update(self):
        #每帧更新
        self.playerInput()
        
        if hasattr(self,"bomb"):
            if self.bomb.isdel:
                del self.bomb
            else:
                self.bomb.updateBomb()
        if self.gameover:
            return 


        self.updateBullet()
        if hasattr(self,"enemy"):
            self.enemy.updateEnemy()
            self.bulletHitEnemy()
            
            if self.enemy.isdel:
                del self.enemy
                self.initNewEnemy()


        self.updateBG()
        self.dprint = "->{}".format(px.frame_count)

    def draw(self):
        if hasattr(self,"bomb"):
            self.bomb.drawBomb()
        if self.gameover:
            px.text(40, px.height/2-32, "Game Over!", px.frame_count % 16)
            px.text(30, px.height/2+8, "Your score is {}.".format(self.score), 7)
            px.text(20, px.height/2+16, "Press Q to exit the Game.".format(self.score), 7)
            return 
        #绘图
        px.cls(0)
        self.player.drawPlayer()
        #背景
        self.displayBG()
        #子弹
        self.displayBullet()
        
        if hasattr(self,"enemy") and self.enemy != None:
            self.enemy.drawEnemy()
            # px.text(0, 4, "Debug:{}".format(str(int(self.player.y))+":"+str(self.player.x)),7)



        px.text(0, 4, "Score:{}".format(self.score), 7)




if __name__ == "__main__":
    App()
