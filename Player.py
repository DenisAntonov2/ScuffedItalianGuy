from pygame import mixer
import MapAndBlocks, PowerUps, Constants, pyxel, math, time

"""THIS IS THE FILE WHERE THE LOGIC FOR THE PLAYER I.E. MARIO IS"""
class Mario():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = Constants.SMALL_MARIO_WIDTH
        self.h = Constants.SMALL_MARIO_HEIGHT
        self.u = Constants.SMALL_MARIO_U
        self.v = Constants.SMALL_MARIO_V
        self.groundFloor = 232 - self.h
        self.lives = Constants.MARIO_LIVES
        self.score = 0

        self.__dx = 1
        self.__dy = 3
        self.__du = 1/8
        self.__gravity = 1

        self.right = True
        self.left = False
        self.jump = False
        self.jumpcounter = 0
        self.showplus10 = 0

    # DRAW FUNCTION WHICH BASICALLY DRAWS THE MARIO SPRITE DEPENDING ON THE ORIENTATION OF MARIO
    def draw(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.right = True
            self.left = False
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.right = False
            self.left = True
        if self.right:
            pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, 6)
        elif self.left:
            pyxel.blt(self.x, self.y, 0, self.u, self.v, -self.w, self.h, 6)

    # FUNCTION WHICH IS RESPONSIBLE FOR THE CORE MOVEMENT OF THE GAME WORKS
    # HEAVILY WITH THE COLLISION FUNCTION
    def marioMove(self, map:MapAndBlocks.Map):
        # THIS IS A CONDITION WHICH STOPS THE MOVEMENT OF MARIO AT THE END OF THE GAME
        if round(map.u) >= 62 and map.v == 96:
            self.dx = 0
            self.dy = 0
            self.du = 0

        # APPLIES GRAVITY
        if self.y < self.groundFloor:
            self.y += self.gravity

        # MOVES MARIO TO THE RIGHT OR MOVES MAP IF MARIO IS AT THE MIDDLE OF THE SCREEN
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x == 128:
                map.u += self.du
                # SINCE THE MAP IN THE EDITOR IS NOT INFINITE WE CHANGE THE "ROW" WITH THE NEXT TWO CONDITIONS
                if round(map.u) == 200 and map.v == 0:
                    map.u = 0
                    map.v = 32
                if round(map.u) == 200 and map.v == 32:
                    map.u = 0
                    map.v = 64
            else:
                self.x += self.dx

        # MOVES MARIO TO THE LEFT
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.dx

        # FUNCTION WHICH ALLOWS MARIO TO JUMP
        if pyxel.btn(pyxel.KEY_UP):
            # JUMP SOUNDS
            jump_sound = mixer.Sound('music/small_jump.ogg')
            jump_sound.set_volume(0.2)
            jump_sound.play()
            # IF THE Y COORDINATE OF MARIO SHOWS THAT MARIO IS ON A SOLID GROUND IT
            # ALLOWS MARIO TO JUMP WHICH IS ONE OF THE CONDITIONS
            if self.y == self.groundFloor:
                self.jump = True
        # IF WE ARE ALLOWED TO JUMP AND OUR COUNTER IS LESS THAN THE
        # MAXIMUM TIME WE ARE ABLE TO JUMP WE MOVE MARIO UP BU ONE UNIT
        if self.jump and self.jumpcounter < 30:
            self.y -= self.dy
            self.jumpcounter += 1
        # WHEN WE ARE DONE WITH OUR JUMP WE RESET THE CONDITION VARIABLES
        if self.jumpcounter == 30:
            self.jumpcounter = 0
            self.jump = False

    # THIS FUNCTION IS RESPONSIBLE FOR THE COLLISIONS WITH BLOCKS AND OTHER FUNCTIONALITY
    def marioCollisionBlock(self, blocks: list, publocks: list ,shroom:PowerUps.Shroom, marker, level):
        self.dx = 1
        self.dy = 3
        self.du = 1/8
        self.gravity = 1
        self.groundFloor = 232 - self.h
        # THIS SERVES THE ROLE OF ALLOWING A MARKER WHICH SHOWS THAT
        # POINTS HAVE BEEN RECEIVED WHEN MARIO COLLECTS THEM FROM A BLOCK
        if self.showplus10 >= 30:
            marker.x = -20
            marker.y = -20
            self.showplus10 = 0
        self.showplus10 += 1
        # IF MARIO FALLS IN A WHOLE IT RESETS THE LEVEL
        if self.y > 240:
            level.u = 1
            level.v = 0
            self.u = Constants.SMALL_MARIO_U
            self.v = Constants.SMALL_MARIO_V
            self.w = Constants.SMALL_MARIO_WIDTH
            self.h = Constants.SMALL_MARIO_HEIGHT
            self.lives -= 1
            self.x = 10
            self.y = 232 - self.h

        # A LOOP THAT GOES THROUGH ALL THE BLOCKS IN THE GAME
        for element in blocks:
            # CHANGES THE CURRENT SOLID GROUND THAT MARION STANDS ON TO RESTRICT GRAVITY AND LET MARIO SIT ON A BLOCK
            if self.y == element.y - self.h and (self.x > element.x - self.w and self.x < element.x + element.w):
                self.groundFloor = element.y - self.h

            # NEXT THREE LOOPS AND CONDITIONS ARE RESPONSIBLE FOR ALLOWING MARIO TO BE ABLE TO FALL IN THE WHOLES
            for i in range(16):
                if math.floor(level.u) >= 130 + i and math.floor(level.u) <= 132 + i and level.v == 0:
                    if self.x <= 128 - 8*i and self.x >= 124 - 8*i:
                        self.groundFloor = 500
            for i in range(16):
                if math.floor(level.u) >= 166 + i and math.floor(level.u) <= 170 + i and level.v == 0:
                    if self.x <= 128 - 8*i and self.x >= 120 - 8*i:
                        if self.y > 102:
                            self.groundFloor = 500
            for i in range(16):
                if math.floor(level.u) >= 158 + i and math.floor(level.u) <= 160 + i and level.v == 32:
                    if self.x <= 128 - 8*i and self.x >= 124 - 8*i:
                        self.groundFloor = 500

            # CHECKS FOR BLOCKS IN FRONT OF MARIO FROM THE RIGHT AND DOESN'T ALLOW HIM TO MOVE IF THERE ARE
            if pyxel.btn(pyxel.KEY_RIGHT):
                if (self.x + self.w == element.x and self.y >= element.y - self.h):
                    if (self.y - element.h >= element.y or self.y + self.h <= element.y):
                        pass
                    else:
                        self.dx = 0
                        self.du = 0

            # CHECKS FOR BLOCKS IN FRONT OF MARIO FROM THE LEFT AND DOESN'T ALLOW HIM TO MOVE IF THERE ARE
            if pyxel.btn(pyxel.KEY_LEFT):
                if (self.x - element.w == element.x and self.y >= element.y - self.h):
                    if (self.y - element.h >= element.y or self.y + self.h <= element.y):
                        pass
                    else:
                        self.dx = 0

            # STOPS MARIO JUMP IF THERE IS A BLOCK ABOVE
            if ((self.x + self.w > element.x and self.x < element.x + element.w) and self.y - 1 == element.y + element.h):
                self.jump = False
                self.jumpcounter = 0
                # IF THE BLOCK ABOVE IS A QUESTION MARK BLOCK
                if element.u == 16 and element.v == 48:
                    # CHANGES THE DESIGN OF THE BLOCK TO A USED QUESTION BLOCK
                    element.v = 64
                    # IF THE QUESTION BLOCK IS IN THIS LIST IT SPAWNS A MUSHROOM
                    if element in publocks:
                        shroom.y = element.y - 16
                        shroom.x = element.x
                        shroom.grow = True
                    # ELSE IT SPAWNS THE MARKER THAT SHOWS THAT POINT WERE COLLECTED
                    else:
                        marker.x = element.x
                        marker.y = element.y - 16
                        self.score += 10

                # SOUND FOR BLOCK COLLISION
                breaking_block_sound = mixer.Sound('music/brick_smash.ogg')
                breaking_block_sound.play()

    # THIS FUNCTION IS RESPONSIBLE FOR THE INTERACTION OF THE ENEMIES
    def marioCollisionEnemy(self, enemies: list, level: MapAndBlocks.Map):
        # GOES THROUGH A LIST OF ALL ENEMIES
        for element in enemies:
            # IF MARIO COLLIDES WITH AN ENEMY FROM THE LEFT OR FROM THE RIGHT
            if (self.x == element.x - self.w and (self.y > element.y - self.h and self.y < element.y + self.h)) \
                    or (self.x == element.x + self.w and (self.y > element.y - self.h and self.y < element.y + self.h)):
                # IF IT IS BIG MARIO IT CHANGES BACK TO SMALL MARIO
                if self.h == 32:
                    killing_enemy = mixer.Sound('music/kick.ogg')
                    killing_enemy.play()
                    self.u = Constants.SMALL_MARIO_U
                    self.v = Constants.SMALL_MARIO_V
                    self.w = Constants.SMALL_MARIO_WIDTH
                    self.h = Constants.SMALL_MARIO_HEIGHT
                    self.y = self.y + Constants.SMALL_MARIO_HEIGHT
                # ELSE IF IT IS SMALL MARIO RESETS THE LEVEL
                else:
                    killing_enemy = mixer.Sound('music/kick.ogg')
                    killing_enemy.play()
                    self.score -= 50
                    self.lives -= 1
                    level.u = 1
                    level.v = 0
                    self.x = 10
                    self.y = 232 - self.h
            # ELSE IF MARIO COLLIDES WITH AN ENEMY FROM ABOVE
            elif (self.y == element.y - self.h and (self.x >= element.x - self.w and self.x <= element.x + self.w)):
                # KILLING THE ENEMY SOUND
                killing_enemy = mixer.Sound('music/kick.ogg')
                killing_enemy.play()
                # ADD TO THE SCORE AND GIVES MARIO A LITTLE BOOST UP THEN IT REMOVES THE ENEMY
                self.score += 50
                self.jump = True
                self.jumpcounter = 15
                element.y = 300

    # THIS FUNCTION ANSWERS FOR THE COLLISION WITH POWER UPS LIKE MUSHROOMS
    def marioCollisionPU(self, shroom):
        # IF THERE IS ANY KIND OF COLLISION OF MARIO WITH THE MUSHROOM
        if ((round(self.x) >= shroom.x - self.w and round(self.x) <= shroom.x + self.w) and (self.y >= shroom.y - self.h and self.y <= shroom.y + self.h)):
            # IF IT IS SMALL MARIO IT TRANSFORMS INTO A BIG MARIO
            if self.h == 16:
                powerup_sound = mixer.Sound('music/powerup.ogg')
                powerup_sound.play()
                self.u = Constants.BIG_MARIO_U
                self.v = Constants.BIG_MARIO_V
                self.w = Constants.BIG_MARIO_WIDTH
                self.h = Constants.BIG_MARIO_HEIGHT
                self.y = self.y - 17
                shroom.y = 300
            # IF IT IS ALREADY BIG MARIO IT ADDS TO THE SCORE
            else:
                shroom.y = 300
                self.score += 300

    # THIS FUNCTION ANSWERS FOR THE RUNNING AND JUMPING ANIMATION OF MARIO
    def changeSprite(self):
        # RUNNING ANIMATION OF SMALL MARIO
        if self.h == 16:
            # IF THE LEFT OR RIGHT BUTTON IS PRESSED THE SPRITE OF MARIO CHANGES EACH SECOND
            if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT)) and self.y == self.groundFloor:
                # EVERY EVEN SECOND WE USE THIS SPRITE
                if round(time.time()) % 2 == 0:
                        self.u = 48
                        self.v = 112
                # EVERY ODD SECOND WE USE THIS SPRITE
                elif round(time.time()) % 2 != 0:
                    self.u = 48
                    self.v = 96
            # OTHERWISE WE USE THE BASIC MARIO SPRITE
            else:
                self.u = Constants.SMALL_MARIO_U
                self.v = Constants.SMALL_MARIO_V
            # IF WE ARE IN THE PROCESS OF JUMPING WE USE THIS SPRITE
            if self.y != self.groundFloor:
                self.u = 48
                self.v = 112
        # RUNNING ANIMATION OF BIG MARIO
        if self.h == 32:
            # IF THE LEFT OR RIGHT BUTTON IS PRESSED THE SPRITE OF MARIO CHANGES EACH SECOND
            if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT)) and self.y == self.groundFloor:
                if round(time.time()) % 2 == 0:
                    self.u = 0
                    self.v = 16
                elif round(time.time()) % 2 != 0:
                    self.u = 0
                    self.v = 48
            # OTHERWISE WE USE THE BASIC MARIO SPRITE
            else:
                self.u = Constants.BIG_MARIO_U
                self.v = Constants.BIG_MARIO_V
            # IF WE ARE IN THE PROCESS OF JUMPING WE USE THIS SPRITE
            if self.y != self.groundFloor:
                self.u = 0
                self.v = 16
############################ SETTERS FOR THE MARIO CLASS
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int and type(x) != float:
            raise TypeError
        if (x >= 0 and x <= 256):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int and type(y) != float:
            raise TypeError
        if y >= 0 and y <= 256:
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
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, lives):
        if type(lives) != int:
            raise TypeError
        if lives >= 0 and lives <= 3:
            self.__lives = lives

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if type(score) != int:
            raise TypeError
        else:
            self.__score = score

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

    @property
    def jump(self):
        return self.__jump

    @jump.setter
    def jump(self, jump):
        if type(jump) != bool:
            raise TypeError
        else:
            self.__jump = jump

    @property
    def jumpcounter(self):
        return self.__jumpcounter

    @jumpcounter.setter
    def jumpcounter(self, jumpcounter):
        if type(jumpcounter) != int:
            raise TypeError
        if jumpcounter >= 0 and jumpcounter <= 30 :
            self.__jumpcounter = jumpcounter

    @property
    def showplus10(self):
        return self.__showplus10

    @showplus10.setter
    def showplus10(self, showplus10):
        if type(showplus10) != int:
            raise TypeError
        if showplus10 >= 0 and showplus10 <= 30:
            self.__showplus10 = showplus10