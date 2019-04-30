import pyxel as px
# from math import cos,sin
import random
__doc__ = """
敌人(第二张图)
飞行模式描述：
[1]
从顶部随机生成，向下直线匀速飞行
[2]
从顶部随机生成，向玩家X轴飞行
[3]
# 从顶部随机生成, 躲避玩家
[4]
从玩家X坐标生成,飞行速度特别快


"""


class Enemy():

    def __init__(self,player:px, moveMode: int, hp: int=1, fireMode: int=0):
        """按照飞行模式和射击模式，血量生成一个敌人"""
        self.player = player
        self.moveMode = moveMode
        self.hp = hp
        self.fireMode = fireMode
        if self.moveMode in [1,2,3,4]:
            self.x = random.randint(8, px.width-8)
        elif self.moveMode in []:
            self.x = self.player.x+8
        else:
            self.x = px.width//2

        self.y = 2

        self.LeftToRight = 16
        #负数上下颠倒
        self.UpToDown = 16 * -1 
        print("已经创建对象:",id(self))
        # self.lv = random.randint(2, 8)
        # self.clr = random.randint(1, 16)
        #标记删除
        self.isdel = False


    def drawEnemy(self):
        #构建敌人
        #飞行模式对应敌机外形图()
        m2p={
            1:0,
            2:2,
            3:1,
            4:3
        }

        picX = 0
        #如没有则使用5号图
        picY = m2p.get(self.moveMode,4) * 16
        #绘图
        px.blt(
            self.x,
            self.y,
            1,
            picY,
            0,
            self.LeftToRight,
            self.UpToDown,
            0
        )

    def __del__(self):
        print("已经销毁:id>{}".format(id(self)))

    def updateEnemy(self):
        #敌人移动轨迹
        if self.moveMode == 1:
            #向下直线匀速飞行
            self.y += 2
        elif self.moveMode == 2:
            #向玩家X轴飞行
            self.y += 1
            if self.x< self.player.x:
                self.x+=1
            elif self.x>self.player.x:
                self.x-=1

        elif self.moveMode == 3:
           # 躲避玩家
            self.y += 1
            if self.x< self.player.x:
                if abs(self.x-self.player.x)<6:
                    self.x = self.x-(6-abs(self.x-self.player.x))
                else:
                    self.x-=1
            elif self.x>self.player.x:
                if abs(self.x-self.player.x)<6:
                    self.x = self.x+(6-(abs(self.x-self.player.x)))
                else:
                    self.x+=1
            if self.x <= 16:
                self.x = 16
            if self.x >= px.width-32:
                self.x = px.width-32
        elif self.moveMode == 4:
            #加速度直线飞行
            if abs(self.x-self.player.x)<24:
                print(abs(self.x-self.player.x))
                if 24-abs(self.x-self.player.x) >8:
                    self.y = self.y+8
                else:
                    self.y = self.y+(24-abs(self.x-self.player.x))
            else:
                self.y =self.y+2
        else:
            #默认模式1
            self.y += 2

        #飞出到底
        if self.y > px.height:
            # self.initEnemy()
            self.y = 0
            # Enemy.delself(self)
            # print(id(self))
            self.isdel = True

        #控制左右飞行
        self.x =max(min(px.width-16,self.x),0)