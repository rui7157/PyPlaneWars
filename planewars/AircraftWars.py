import pyxel as px
import glfw

__doc__="""
飞机大战游戏

"""

class App:
    def __init__(self):
        px.init(123, 200,scale=0)
        px.load("AircraftWars.pyxel")
        #调试信息
        self.dprint = "" 

        self.playerX = px.width/2-8
        self.playerY = px.height-16
        self.playerAnim = 16
        self.lrKey = ""
        self.playerLeftToRight = 16
        self.playerUpToDown = 16
        self.bx = self.playerX+8
        self.by = self.playerY-8
        self.initBG()
        px.mouse=True
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
            self.dprint="press LEFT"

        if px.btnp(px.KEY_RIGHT):
            self.lrKey = "right"
            self.playerLeftToRight = -16
            self.playerAnim = 64
            # print("press RIGHT")
            self.dprint="press RIGHT"
            
        if px.btnr(px.KEY_LEFT) or px.btnr(px.KEY_RIGHT):
            self.lrKey=""


    def _updateAnimate(self,objName:str,firstGrid,width,anmCount,pl=4):
        """循环播放"""
        #对象名字(self.playerAnim),起始X坐标,图片宽度,图片数量,动画频率
        objAnimValue = getattr(self,objName)
        # objAnim = 200
        # print(self.playerAnim)
        if px.frame_count%pl==0:
            objAnimValue+=width
            setattr(self,objName,objAnimValue)
            if objAnimValue>=firstGrid+width*anmCount:
                objAnimValue=firstGrid
                setattr(self,objName,objAnimValue)
        # print(getattr(self,objName))

    def disposableAnim(self,objName:str,firstGrid,width,anmCount,pl=2):
        #一次性动画
        # setattr(self,objName,firstGrid)
        objAnimValue = getattr(self,objName)
        if px.frame_count%pl==0:
            objAnimValue+=width
            setattr(self,objName,objAnimValue)
            if objAnimValue>=firstGrid+width*anmCount:
                # objAnimValue=firstGrid
                setattr(self,objName,firstGrid+width*(anmCount-1))


    def updateAirAnimate(self,dire=""):
        #飞机动画
        
        if dire =="left":
            self.disposableAnim("playerAnim",64,16,2,10)
        elif dire == "right":
            self.disposableAnim("playerAnim",64,16,2,10)
        else:
            self._updateAnimate("playerAnim",0,16,4)


    def updateBullet(self):
        #更新子弹
        # self.bullet = 
        self.by-=2
        if self.by<=0:
            self.by = self.playerY
            self.bx = self.playerX+8
        # for y in range(2,self.playerY-8):
        #     if y%5==0:
        #         px.rect(self.playerX+8, self.playerY-y, self.playerX+8, self.playerY-y, 7)




    def initBG(self):
        #初始化背景
        self.bgx = 0
        self.bgy = 0

    def displayBG(self):
        bgWidth = 1
        bgHeight = 8
        #背景左边
        px.rect(self.bgx,self.bgy,self.bgx+bgWidth-1,self.bgy+bgHeight,6)
        #背景右边
        px.rect(self.bgx+px.width-1,self.bgy,self.bgx+px.width+bgWidth-1,self.bgy+bgHeight,6)


    def updateBG(self):
        self.bgy+=16
        if self.bgy>=px.height:
            self.bgy = 0



    def update(self):
        #每帧更新
        self.playerInput()

        self.updateBullet()
        #动画区域firstGrid-endGrid
        self.updateAirAnimate(self.lrKey)
        self.updateBG()
        self.dprint="->{}".format(px.frame_count)


    def draw(self):
        #绘图
        px.cls(0)
        px.rect(self.bx ,self.by, self.bx, self.by, 7)
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
        self.displayBG()
        self.updateBullet()
        
        # px.text(5,4,"this a game deme ",7)
        px.text(5,4,"Debug:{}".format(self.dprint),7)


App()