import pyxel as px
import random
__doc__ = """
敌人(第二张图)
飞行模式描述：
[1]
从顶部随机生成，向下直线匀速飞行
[2]
从顶部随机生成，向玩家X轴飞行
[3]
从顶部随机生成, 选择玩家方向直线飞行
[4]
从玩家X坐标生成,飞行速度特别快


"""


class Enemy():

    def __init__(self,player:px, moveMode: int, hp: int, fireMode: int):
        """按照飞行模式和射击模式，血量生成一个敌人"""
        self.moveMode = moveMode
        self.hp = hp
        self.fireMode = fireMode
        self.player = player
        self.eX = random.randint(2, px.width-2)
        self.eY = 2
        self.lv = random.randint(2, 8)
        self.clr = random.randint(1, 16)

    def drawEnemy(self):
        #构建敌人
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

Enemy(1,1,1,1)