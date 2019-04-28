import pyxel as px
import glfw

__doc__="""
火炬动画练习

"""

class App:
    def __init__(self):
        px.init(255, 200,scale=0)
        px.load("lianxipixDraw.pyxel")
        self.fireX = 64
        self.fireY = 64
        self.fireAnim = 0
        px.mouse=True


        px.run_with_profiler(self.update, self.draw)

    def update(self):

        
        if px.frame_count%4==0:
            self.fireAnim+=8
            if self.fireAnim>=8*6:self.fireAnim=0
            

    def draw(self):
        px.cls(0)
        px.blt(
            self.fireX,
            self.fireY,
            0,
            self.fireAnim,
            64,
            8,
            16,
            12
        )
        px.blt(
                self.fireX+16,
                self.fireY,
                0,
                self.fireAnim,
                64,
                8,
                16,
                12
            )
        px.blt(
                self.fireX+32,
                self.fireY,
                0,
                self.fireAnim,
                64,
                8,
                16,
                12
            )
        px.text(5,4,"this a fire animation deme ",1)

App()