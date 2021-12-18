import pyxel

# CLASS FOR THE MAP OR THE LEVEL
class Map:
    def __init__(self):
        self.tm = 0
        self.u = 0
        self.v = 0
        self.w = 32
        self.h = 32

    def draw(self):
        pyxel.bltm(0, 0, self.tm, self.u, self.v, self.w, self.h)

    @property
    def tm(self):
        return self.__tm

    @tm.setter
    def tm(self, tm):
        if type(tm) != int:
            raise TypeError
        else:
            self.__tm = tm

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, w):
        if type(w) != int:
            raise TypeError
        else:
            self.__w = w

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if type(h) != int:
            raise TypeError
        else:
            self.__h = h

    @property
    def u(self):
        return self.__u

    @u.setter
    def u(self, u):
        if type(u) != int and type(u) !=  float:
            raise TypeError
        else:
            self.__u = u

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if type(v) != int:
            raise TypeError
        else:
            self.__v = v


# CLASS FOR THE MARKERS OF THE TEXT THAT SHOWS UP
class Marker:
    def __init__(self, x, y, text:str):
        self.x = x
        self.y = y
        self.text = text

    def draw(self):
        pyxel.text(self.x, self.y, self.text, pyxel.COLOR_WHITE)

# CLASS FOR THE BLOCKS AS WHOLE (MOTHER CLASS FOR THE BLOCKS
class Block():
    def __init__(self, x, y, u, v):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = 16
        self.h = 16

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, 16, 16)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int and type(x) != float:
            raise TypeError
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int and type(y) != float:
            raise TypeError
        else:
            self.__y = y

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, w):
        if type(w) != int:
            raise TypeError
        else:
            self.__w = w

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if type(h) != int:
            raise TypeError
        else:
            self.__h = h

    @property
    def u(self):
        return self.__u

    @u.setter
    def u(self, u):
        if type(u) != int:
            raise TypeError
        else:
            self.__u = u

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if type(v) != int:
            raise TypeError
        else:
            self.__v = v


class groundBlock(Block):
    def __init__(self, x, y, u = 16, v = 32):
        super().__init__(x,y,u,v)


########################################## DIFFERENT KIND OF BLOCKS
class brickBlock(Block):
    def __init__(self, x, y, u = 16, v = 16):
        super().__init__(x,y,u,v)


class sblock(Block):
    def __init__(self, x, y, u = 32, v = 64):
        super().__init__(x,y,u,v)


class Pipe(Block):
    def __init__(self, x, y, u = 0, v = 160):
        super().__init__(x, y, u, v)
        self.w = 32
        self.h = 32

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, 32, self.h, 6)


class Qblock(Block):
    def __init__(self, x, y, u=16, v=48):
        super().__init__(x, y, u, v)


# A FUNCTION THAT GOES THROUGH A LIST OF OBJECTS AND MOVES THEM WHEN THE MAP MOVES
def Interaction(somel:list, player):
    for element in somel:
        if pyxel.btn(pyxel.KEY_RIGHT):
            if player.x == 128 and player.dx != 0:
                element.x -= 1
        if element.x < -element.w:
            element.y = -40

