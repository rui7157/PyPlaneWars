import pyxel as px


class BGM():

    def __init__(self):
        # px.init(10,10)
        # px.load("AircraftWars.pyxel")
        px.sound(5).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )

        px.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )

        px.sound(2).set(
            "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        px.sound(3).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        px.sound(4).set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25
        )

        px.play(0, [5, 1], loop=True)
        px.play(1, [2, 3], loop=True)
        px.play(2, 4, loop=True)

        # px.run(self.draw,self.update)
    def stop(self):
        px.stop()

    def bombSound(self):
        px.play(0, 0, loop=False)

    def bulletSound(self):
        px.play(0, 6, loop=False)

    def gameoverSound(self):
        px.play(0, 7, loop=False)
