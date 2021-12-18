import pyxel


class PowerUp:
    def __init__(self, x, y, w, h = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.dx = 1
        self.groundFloor = 216
        self.grow = False

##### SETTERS FOR THE POWER UPS
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

    @property
    def groundFloor(self):
        return self.__groundFloor

    @groundFloor.setter
    def groundFloor(self, groundFloor):
        if type(groundFloor) != int:
            raise TypeError
        else:
            self.__groundFloor = groundFloor

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
    def grow(self):
        return self.__grow

    @grow.setter
    def grow(self, grow):
        if type(grow) != bool:
            raise TypeError
        else:
            self.__grow = grow


# CLASS FOR THE MUSHROOM POWER UP
class Shroom(PowerUp):
    def __init__(self, x, y, w=16, h = 0):
        super(Shroom, self).__init__(x, y, w, h)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 48, 48, self.w, self.h, 6)

    # A FUNCTION THAT ANSWERS FOR THE MOVEMENT OF THE MUSHROOM WHEN IT IS SPAWNED
    def movePU(self, blocks):
        self.groundFloor = 216

        # IF THE MUSHROOM IS SPAWNED IT SETS ITS HEIGHT TO 0 AND ALLOWS IT TO GROW
        if self.x < -16:
            self.grow = False
            self.h = 0

        #GROWS UNTIL FULL SIZE
        if self.grow:
            if self.h >= 0 and self.h < 16:
                self.h += 1

        # IF IT IS FULL SIZE STARTS TO MOVE
        if self.h == 16:
            # GOES THROUGH ALL THE BLOCKS
            for element in blocks:
                # IF IT IS ON THE BLOCK IT SITS ON IT
                if self.y == element.y - self.h and (self.x > element.x - self.w and self.x < element.x + element.w):
                    self.groundFloor = element.y - self.h

                # IF IT COLLIDES WITH A BLOCK CHANGES DIRECTION
                if (self.x + self.w == element.x):
                    if ((self.y - self.h >= element.y or self.y + self.h <= element.y) and not (element.u == 0 and element.v == 160)):
                        pass
                    else:
                        self.dx = -1
                if (self.x - element.w == element.x):
                    if ((self.y - self.h >= element.y or self.y + self.h <= element.y) and not (element.u == 0 and element.v == 160)):
                        pass
                    else:
                        self.dx = 1
            # MOVES
            self.x += self.dx
            # APPLIES GRAVITY IF IT IS NOT ON A SOLID GROUND
            if self.y < self.groundFloor:
                self.y += 1