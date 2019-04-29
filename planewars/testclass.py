
class a():
    x =1
    y =1

a().x = 2

class b(a):
    def __init__(self):
        pass

    def getaattr(self):
        print(a.x)

b().getaattr()