import math, pyxel, Player, Enemies, MapAndBlocks, PowerUps, time

from pygame import mixer

# MUSIC THEME
mixer.init()
main_theme = mixer.Sound('music/main_theme.ogg')
main_theme.play()


class Game:
    def __init__(self):
        # INITIALIZES THE GAME
        pyxel.init(256, 256, scale=8, caption="Scuffed Mario", fps=60, fullscreen=True)
        pyxel.load("assets/resources.pyxres")

        # INITIALIZES MARIO
        self.player = Player.Mario(10, 200)

        # INITIALIZES THE MAP
        self.level = MapAndBlocks.Map()
        # INITIALIZES THE TIME
        self.time = 400
        # INITIALIZES THE MARKERS OR THE TEXT
        self.marker1 = MapAndBlocks.Marker(50, 20, ("MARIO\n" + str.zfill(str(self.player.score), 6)))
        self.marker2 = MapAndBlocks.Marker(200, 20, "LIVES\n" + str.zfill(str(self.player.lives), 3))
        self.marker3 = MapAndBlocks.Marker(140, 20, "WORLD\n 1-1")
        self.marker4 = MapAndBlocks.Marker(170, 20, ("TIME\n" + str.zfill(str(math.ceil(self.time)), 3)))
        self.marker5 = MapAndBlocks.Marker(-20, -20, '+10')

        # INITIALIZES THE BRICK BLOCKS
        self.bblock1 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock2 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock3 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock4 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock5 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock6 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock7 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock8 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock9 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock10 = MapAndBlocks.brickBlock(-20, -20)
        self.bblock11 = MapAndBlocks.brickBlock(-20, -20)

        # INITIALIZES THE QUESTION MARK BLOCKS
        self.qblock1 = MapAndBlocks.Qblock(-20, -20)
        self.qblock2 = MapAndBlocks.Qblock(-20, -20)
        self.qblock3 = MapAndBlocks.Qblock(-20, -20)
        self.qblock4 = MapAndBlocks.Qblock(-20, -20)
        self.qblock5 = MapAndBlocks.Qblock(-20, -20)
        self.qblock6 = MapAndBlocks.Qblock(-20, -20)

        # INITIALIZES THE PIPES
        self.pblock1 = MapAndBlocks.Pipe(-40, -40)
        self.pblock2 = MapAndBlocks.Pipe(-40, -40)
        self.pblock3 = MapAndBlocks.Pipe(-40, -40)
        self.pblock4 = MapAndBlocks.Pipe(-40, -40)

        # INITIALIZES THE STRONG BLOCKS USED FOR STAIRS
        self.sblock1 = MapAndBlocks.sblock(-40, -40)
        self.sblock2 = MapAndBlocks.sblock(-40, -40)
        self.sblock3 = MapAndBlocks.sblock(-40, -40)
        self.sblock4 = MapAndBlocks.sblock(-40, -40)
        self.sblock5 = MapAndBlocks.sblock(-40, -40)
        self.sblock6 = MapAndBlocks.sblock(-40, -40)
        self.sblock7 = MapAndBlocks.sblock(-40, -40)
        self.sblock8 = MapAndBlocks.sblock(-40, -40)
        self.sblock9 = MapAndBlocks.sblock(-40, -40)
        self.sblock10 = MapAndBlocks.sblock(-40, -40)
        self.sblock11 = MapAndBlocks.sblock(-40, -40)
        self.sblock12 = MapAndBlocks.sblock(-40, -40)
        self.sblock13 = MapAndBlocks.sblock(-40, -40)
        self.sblock14 = MapAndBlocks.sblock(-40, -40)
        self.sblock15 = MapAndBlocks.sblock(-40, -40)
        self.sblock16 = MapAndBlocks.sblock(-40, -40)
        self.sblock17 = MapAndBlocks.sblock(-40, -40)
        self.sblock18 = MapAndBlocks.sblock(-40, -40)
        self.sblock19 = MapAndBlocks.sblock(-40, -40)
        self.sblock20 = MapAndBlocks.sblock(-40, -40)
        self.sblock21 = MapAndBlocks.sblock(-40, -40)
        self.sblock22 = MapAndBlocks.sblock(-40, -40)
        self.sblock23 = MapAndBlocks.sblock(-40, -40)
        self.sblock24 = MapAndBlocks.sblock(-40, -40)

        # CONSTRUCTS A LIST WITH ALL THE BLOCKS
        self.blocks = [self.bblock1, self.bblock2, self.bblock3, self.bblock4, self.bblock5,
                       self.bblock6, self.bblock7, self.bblock8, self.bblock9, self.bblock10, self.bblock11,
                       # QUESTION BLOCKS
                       self.qblock1, self.qblock2, self.qblock3, self.qblock4, self.qblock5, self.qblock6,
                       # PIPES
                       self.pblock1, self.pblock2, self.pblock3, self.pblock4,
                       # STRONG BLOCKS
                       self.sblock1, self.sblock2, self.sblock3, self.sblock4, self.sblock5, self.sblock6, self.sblock7,
                       self.sblock8, self.sblock9, self.sblock10, self.sblock11, self.sblock12, self.sblock13,
                       self.sblock14,
                       self.sblock15, self.sblock16, self.sblock17, self.sblock18, self.sblock19, self.sblock20,
                       self.sblock21,
                       self.sblock22, self.sblock23, self.sblock24]

        # INITIALIZES THE ENEMIES
        self.enemy1 = Enemies.Goomba(-20, -20)
        self.enemy2 = Enemies.Koopa(-30, -30)
        self.enemy3 = Enemies.Goomba(-20, -20)
        self.enemy4 = Enemies.Goomba(-20, -20)
        # CONSTRUCTS A LIST FOR ALL ENEMIES
        self.enemies = [self.enemy1, self.enemy2, self.enemy3, self.enemy4]

        # INITIALIZES THE MUSHROOM
        self.shroom = PowerUps.Shroom(300, 300)

        pyxel.run(self.update, self.draw)

    def update(self):
        # CHANGES TIME
        self.time -= (1 / 60)
        # APPLIES CHANGED TIME TO THE MARKER
        self.marker4 = MapAndBlocks.Marker(170, 20, ("TIME\n" + str.zfill(str(math.ceil(self.time)), 3)))
        # IF LIVES HAVE CHANGED IT APPLIES IT TO THE MARKER
        self.marker2 = MapAndBlocks.Marker(200, 20, "LIVES\n" + str.zfill(str(self.player.lives), 3))
        # IF SCORE HAS CHANGED IT APPLIES IT TO THE MARKER
        self.marker1 = MapAndBlocks.Marker(50, 20, ("MARIO\n" + str.zfill(str(self.player.score), 6)))

        # CALLS THE BLOCK COLLISION FUNCTION
        self.player.marioCollisionBlock(self.blocks, [self.qblock1], self.shroom, self.marker5, self.level)

        # CALLS THE ENEMY COLLISION FUNCTION
        self.player.marioCollisionEnemy(self.enemies, self.level)

        # CALLS THE POWER UP COLLISION FUNCTION
        self.player.marioCollisionPU(self.shroom)

        # CALLS THE RUNNING ANIMATION FUNCTION
        self.player.changeSprite()

        # CALLS THE MOVEMENT FUNCTION
        self.player.marioMove(self.level)

        # CALLS THE FUNCTION THAT MOVES THE NEUTRAL OBJECTS ALONG WITH THE MAP
        MapAndBlocks.Interaction(self.enemies, self.player)
        MapAndBlocks.Interaction(self.blocks, self.player)
        MapAndBlocks.Interaction([self.shroom], self.player)

        # CALLS THE ENEMY MOVEMENT AND COLLISION FUNCTION
        self.enemy1.moveEnemy(self.blocks)
        self.enemy2.moveEnemy(self.blocks)
        self.enemy3.moveEnemy(self.blocks)
        self.enemy4.moveEnemy(self.blocks)

        # CALLS THE MUSHROOM MOVEMENT AND COLLISION FUNCTION
        self.shroom.movePU(self.blocks)

        ########################## CONDITIONS FOR THE PLACEMENT OF BLOCKS AND ENEMIES ON THE MAP AT THE RIGHT MOMENT
        if round(self.level.u) == 1 and self.level.v == 0:
            for element in self.blocks:
                element.x = -40
                element.y = -40

            self.qblock2.v = 48
            self.qblock2.x = 272 - 16
            self.qblock2.y = 176

            self.bblock1.x = 272 + 2 * 16
            self.bblock1.y = 176

            self.qblock1.v = 48
            self.qblock1.x = 272 + 3 * 16
            self.qblock1.y = 176

            self.bblock2.x = 272 + 4 * 16
            self.bblock2.y = 176

            self.qblock3.v = 48
            self.qblock3.x = 272 + 5 * 16
            self.qblock3.y = 176

            self.enemy4.x = 272 + 5 * 16
            self.enemy4.y = 232 - self.enemy4.h

            self.bblock3.x = 272 + 6 * 16
            self.bblock3.y = 176

            self.qblock4.v = 48
            self.qblock4.x = 272 + 4 * 16
            self.qblock4.y = 94

            self.pblock1.x = 272 + 12 * 16
            self.pblock1.y = 200

            self.pblock2.x = 272 + 22 * 16
            self.pblock2.y = 192
            self.pblock2.h = 40

            self.pblock3.x = 272 + 32 * 16
            self.pblock3.y = 184
            self.pblock3.h = 48

            self.enemy1.x = 272 + 31 * 16
            self.enemy1.y = 232 - self.enemy1.h

            self.pblock4.x = 272 + 42 * 16
            self.pblock4.y = 184
            self.pblock4.h = 48

            self.enemy2.x = 272 + 35 * 16
            self.enemy2.y = 232 - self.enemy2.h

            self.enemy3.x = 272 + 39 * 16
            self.enemy3.y = 232 - self.enemy3.h

        if round(self.level.u) == 135 and self.level.v == 0:
            self.enemy1.x = 272 + 4 * 16
            self.enemy1.y = 232 - self.enemy1.h

            self.enemy3.x = 272 + 6 * 16
            self.enemy3.y = 232 - self.enemy3.h

            self.bblock1.x = 272
            self.bblock1.y = 176

            self.qblock1.v = 48
            self.qblock1.x = 272 + 16
            self.qblock1.y = 176

            self.bblock2.x = 272 + 2 * 16
            self.bblock2.y = 176

            self.bblock3.x = 272 + 3 * 16
            self.bblock3.y = 118

            self.bblock4.x = 272 + 4 * 16
            self.bblock4.y = 118

            self.bblock5.x = 272 + 5 * 16
            self.bblock5.y = 118

            self.bblock6.x = 272 + 6 * 16
            self.bblock6.y = 118

            self.bblock7.x = 272 + 7 * 16
            self.bblock7.y = 118

            self.bblock8.x = 272 + 8 * 16
            self.bblock8.y = 118

            self.bblock9.x = 272 + 11 * 16
            self.bblock9.y = 118

            self.bblock10.x = 272 + 12 * 16
            self.bblock10.y = 118

            self.qblock2.v = 48
            self.qblock2.x = 272 + 13 * 16
            self.qblock2.y = 118

            self.bblock11.x = 272 + 13 * 16
            self.bblock11.y = 176

        if round(self.level.u) == 1 and self.level.v == 32:
            self.enemy1.x = 272 + 16
            self.enemy1.y = 232 - self.enemy1.h

            self.enemy2.x = 272 + 2 * 16
            self.enemy2.y = 232 - self.enemy2.h

            self.bblock1.x = 272
            self.bblock1.y = 176

            self.bblock2.x = 272 + 16
            self.bblock2.y = 176

            self.qblock4.v = 48
            self.qblock4.x = 272 + 5 * 16
            self.qblock4.y = 176

            self.qblock2.v = 48
            self.qblock2.x = 272 + 8 * 16
            self.qblock2.y = 176

            self.qblock3.v = 48
            self.qblock3.x = 272 + 11 * 16
            self.qblock3.y = 176

            self.qblock1.v = 48
            self.qblock1.x = 272 + 8 * 16
            self.qblock1.y = 118

            self.bblock3.x = 272 + 16 * 16
            self.bblock3.y = 176

            self.bblock4.x = 272 + 19 * 16
            self.bblock4.y = 118

            self.bblock5.x = 272 + 20 * 16
            self.bblock5.y = 118

            self.bblock6.x = 272 + 21 * 16
            self.bblock6.y = 118

        if round(self.level.u) == 50 and self.level.v == 32:
            self.bblock7.x = 272
            self.bblock7.y = 118

            self.qblock5.v = 48
            self.qblock5.x = 272 + 16
            self.qblock5.y = 118

            self.qblock6.v = 48
            self.qblock6.x = 272 + 2 * 16
            self.qblock6.y = 118

            self.bblock8.x = 272 + 3 * 16
            self.bblock8.y = 118

            self.enemy1.x = 272 + 3 * 16
            self.enemy1.y = 232 - self.enemy1.h

            self.enemy2.x = 272 + 2 * 16
            self.enemy2.y = 232 - self.enemy2.h

            self.enemy3.x = 272 + 16
            self.enemy3.y = 232 - self.enemy3.h

            self.enemy4.x = 272 - 16
            self.enemy4.y = 232 - self.enemy4.h

            self.bblock9.x = 272 + 16
            self.bblock9.y = 176

            self.bblock10.x = 272 + 2 * 16
            self.bblock10.y = 176

        if round(self.level.u) == 75 and self.level.v == 32:
            self.sblock1.x = 272
            self.sblock1.y = 216

            self.sblock2.x = 272 + 16
            self.sblock2.y = 216

            self.sblock3.x = 272 + 2 * 16
            self.sblock3.y = 216

            self.sblock4.x = 272 + 3 * 16
            self.sblock4.y = 216

            self.sblock5.x = 272 + 16
            self.sblock5.y = 200

            self.sblock6.x = 272 + 2 * 16
            self.sblock6.y = 200

            self.sblock7.x = 272 + 3 * 16
            self.sblock7.y = 200

            self.sblock8.x = 272 + 2 * 16
            self.sblock8.y = 184

            self.sblock9.x = 272 + 3 * 16
            self.sblock9.y = 184

            self.sblock10.x = 272 + 3 * 16
            self.sblock10.y = 168

            self.sblock11.x = 272 + 9 * 16
            self.sblock11.y = 216

            self.sblock12.x = 272 + 8 * 16
            self.sblock12.y = 216

            self.sblock13.x = 272 + 7 * 16
            self.sblock13.y = 216

            self.sblock14.x = 272 + 6 * 16
            self.sblock14.y = 216

            self.sblock15.x = 272 + 8 * 16
            self.sblock15.y = 200

            self.sblock16.x = 272 + 7 * 16
            self.sblock16.y = 200

            self.sblock17.x = 272 + 6 * 16
            self.sblock17.y = 200

            self.sblock18.x = 272 + 7 * 16
            self.sblock18.y = 184

            self.sblock19.x = 272 + 6 * 16
            self.sblock19.y = 184

            self.sblock20.x = 272 + 6 * 16
            self.sblock20.y = 168

        if round(self.level.u) == 130 and self.level.v == 32:
            self.sblock1.x = 272
            self.sblock1.y = 216

            self.sblock2.x = 272 + 16
            self.sblock2.y = 216

            self.sblock3.x = 272 + 2 * 16
            self.sblock3.y = 216

            self.sblock4.x = 272 + 3 * 16
            self.sblock4.y = 216

            self.sblock5.x = 272 + 16
            self.sblock5.y = 200

            self.sblock6.x = 272 + 2 * 16
            self.sblock6.y = 200

            self.sblock7.x = 272 + 3 * 16
            self.sblock7.y = 200

            self.sblock8.x = 272 + 2 * 16
            self.sblock8.y = 184

            self.sblock9.x = 272 + 3 * 16
            self.sblock9.y = 184

            self.sblock10.x = 272 + 3 * 16
            self.sblock10.y = 168

            self.sblock21.x = 272 + 4 * 16
            self.sblock21.y = 168

            self.sblock22.x = 272 + 4 * 16
            self.sblock22.y = 184

            self.sblock23.x = 272 + 4 * 16
            self.sblock23.y = 200

            self.sblock24.x = 272 + 4 * 16
            self.sblock24.y = 216

            self.sblock11.x = 272 + 10 * 16
            self.sblock11.y = 216

            self.sblock12.x = 272 + 9 * 16
            self.sblock12.y = 216

            self.sblock13.x = 272 + 8 * 16
            self.sblock13.y = 216

            self.sblock14.x = 272 + 7 * 16
            self.sblock14.y = 216

            self.sblock15.x = 272 + 9 * 16
            self.sblock15.y = 200

            self.sblock16.x = 272 + 8 * 16
            self.sblock16.y = 200

            self.sblock17.x = 272 + 7 * 16
            self.sblock17.y = 200

            self.sblock18.x = 272 + 8 * 16
            self.sblock18.y = 184

            self.sblock19.x = 272 + 7 * 16
            self.sblock19.y = 184

            self.sblock20.x = 272 + 7 * 16
            self.sblock20.y = 168

        if round(self.level.u) == 157 and self.level.v == 32:
            self.enemy1.x = 272 + 11 * 16
            self.enemy1.y = 232 - self.enemy1.h

            self.enemy2.x = 272 + 10 * 16
            self.enemy2.y = 232 - self.enemy2.h

            self.enemy3.x = 272 + 16
            self.enemy3.y = 232 - self.enemy3.h

            self.pblock1.x = 272 + 2 * 16
            self.pblock1.y = 200

            self.bblock1.x = 272 + 8 * 16
            self.bblock1.y = 176

            self.bblock2.x = 272 + 9 * 16
            self.bblock2.y = 176

            self.qblock2.v = 48
            self.qblock2.x = 272 + 10 * 16
            self.qblock2.y = 176

            self.bblock3.x = 272 + 11 * 16
            self.bblock3.y = 176

        if round(self.level.u) == 0 and self.level.v == 64:
            self.sblock1.x = 272 + 16
            self.sblock1.y = 216

            self.sblock2.x = 272 + 2 * 16
            self.sblock2.y = 216 - 16

            self.sblock3.x = 272 + 3 * 16
            self.sblock3.y = 216 - 2 * 16

            self.sblock4.x = 272 + 4 * 16
            self.sblock4.y = 216 - 3 * 16

            self.sblock5.x = 272 + 5 * 16
            self.sblock5.y = 216 - 4 * 16

            self.sblock6.x = 272 + 6 * 16
            self.sblock6.y = 216 - 5 * 16

            self.sblock7.x = 272 + 7 * 16
            self.sblock7.y = 216 - 6 * 16

            self.sblock8.x = 272 + 8 * 16
            self.sblock8.y = 216 - 7 * 16

            self.sblock9.x = 272 + 9 * 16
            self.sblock9.y = 216 - 7 * 16

            self.sblock10.x = 272 + 9 * 16
            self.sblock10.y = 216 - 6 * 16

            self.sblock11.x = 272 + 9 * 16
            self.sblock11.y = 216 - 5 * 16

            self.sblock12.x = 272 + 9 * 16
            self.sblock12.y = 216 - 4 * 16

            self.sblock13.x = 272 + 9 * 16
            self.sblock13.y = 216 - 3 * 16

            self.sblock14.x = 272 + 9 * 16
            self.sblock14.y = 216 - 2 * 16

            self.sblock15.x = 272 + 9 * 16
            self.sblock15.y = 216 - 16

            self.sblock16.x = 272 + 9 * 16
            self.sblock16.y = 216

        if round(self.level.u) == 35 and self.level.v == 64:
            self.sblock20.x = 272
            self.sblock20.y = 216

        # REACHES THE FINAL TELEPORTS TO THE FINAL SCREEN
        if round(self.level.u) == 62 and self.level.v == 64:
            main_theme.stop()
            stage_clear = mixer.Sound('music/stage_clear.ogg')
            stage_clear.play()
            self.level.u = 63
            self.level.v = 96

        # IF WE ARE OUT OF LIVES OR OUT OF TIME WE QUIT
        if self.player.lives == 0 or self.time == 0:
            main_theme.stop()
            gameover = mixer.Sound('music/game_over.ogg')
            gameover.play()
            time.sleep(5)
            pyxel.quit()

    def draw(self):
        # INVOKE DRAW FUNCTIONS FOR OBJECTS
        pyxel.cls(0)
        self.level.draw()
        self.marker1.draw()
        self.marker2.draw()
        self.marker3.draw()
        self.marker4.draw()
        self.marker5.draw()

        self.bblock1.draw()
        self.bblock2.draw()
        self.bblock3.draw()
        self.bblock4.draw()
        self.bblock5.draw()
        self.bblock6.draw()
        self.bblock7.draw()
        self.bblock8.draw()
        self.bblock9.draw()
        self.bblock10.draw()
        self.bblock11.draw()

        self.qblock1.draw()
        self.qblock2.draw()
        self.qblock3.draw()
        self.qblock4.draw()
        self.qblock5.draw()
        self.qblock6.draw()

        self.pblock1.draw()
        self.pblock2.draw()
        self.pblock3.draw()
        self.pblock4.draw()

        self.player.draw()

        self.enemy1.draw()
        self.enemy2.draw()
        self.enemy3.draw()
        self.enemy4.draw()

        self.shroom.draw()

# INVOKE THE GAME
Game()
