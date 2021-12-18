import pyxel

class Enemy:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.dx = -1
        self.left = True
        self.right = False

    # A FUNCTION THAT ANSWERS FOR THE MOVEMENT OF THE ENEMIES AND THEIR COLLISIONS WITH BLOCKS
    def moveEnemy(self, blocks):
        # GOES THROUGH EVERY BLOCK
        for element in blocks:
            # IF THERE IS A BLOCK TO THE RIGHT
            if (self.x + self.w == element.x):
                # IF THAT BLOCK IS ABOVE OR UNDER THE ENEMY
                if ((self.y - self.h >= element.y or self.y + self.h <= element.y) and not (element.u == 0 and element.v == 160)):
                    pass
                # IF IT IS NOT CHANGE THE DIRECTION OF THE ENEMY
                else:
                    self.dx = -1
                    self.left = True
                    self.right = False
            # IF THERE IS A BLOCK TO THE LEFT
            if (self.x - element.w == element.x):
                # IF THAT BLOCK IS ABOVE OR UNDER THE ENEMY
                if ((self.y - self.h >= element.y or self.y + self.h <= element.y) and not (element.u == 0 and element.v == 160)):
                    pass
                # IF IT IS NOT CHANGE THE DIRECTION OF THE ENEMY
                else:
                    self.dx = 1
                    self.left = False
                    self.right = True
        # MOVE THE ENEMY
        self.x += self.dx
################## SETTERS FOR THE ENEMY CLASS
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
    def dx(self):
        return self.__dx

    @dx.setter
    def dx(self, dx):
        if type(dx) != int:
            raise TypeError
        else:
            self.__dx = dx

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
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        if type(right) != bool:
            raise TypeError
        else:
            self.__right = right

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        if type(left) != bool:
            raise TypeError
        else:
            self.__left = left

# GOOMBA CLASS
class Goomba(Enemy):
    def __init__(self, x, y, w = 16, h = 16):
        super(Goomba, self).__init__(x, y, w, h)

    def draw(self):
        if self.right:
            pyxel.blt(self.x, self.y, 0, 48, 0, self.w, self.h, 6)
        else:
            pyxel.blt(self.x, self.y, 0, 48, 0, self.w, self.h, 6)

# KOOPA CLASS
class Koopa(Enemy):
    def __init__(self, x, y, w = 16, h = 25):
        super(Koopa, self).__init__(x, y, w, h)

    def draw(self):
        if self.right:
            pyxel.blt(self.x, self.y, 0, 32, 32, -self.w, self.h, 6)
        else:
            pyxel.blt(self.x, self.y, 0, 32, 32, self.w, self.h, 6)
