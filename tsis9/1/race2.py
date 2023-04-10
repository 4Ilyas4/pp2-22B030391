import pygame as pg
import random
pg.init()
Bg = pg.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\2\\Bg.png")
Br= Bg.get_rect()
Bw, Bh = Br[2],Br[3]
W = Bw
H = Bh
fps = 30
WHITE = ((255,255,255))
RED = ((255,0,0))
GREEN = ((0,255,0))
BLACK = ((0,0,0))
scr = pg.display.set_mode((W,H))
clock = pg.time.Clock()
my_font = pg.font.SysFont('Verdana', 20)
game_over = my_font.render("Game Over", True, RED)
NeW = my_font.render("New Game", True, GREEN)
N = 5
score = 0
coins = 0
over = 0 
class Coin():
    def __init__(self,x):
        self.y = 0
        self.x = x
        self.im = pg.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\2\\Coin.png")
        self.rect = self.im.get_rect()
        self.w, self.h = self.rect[2], self.rect[3]
        self.dy = 10
        self.weight = 1
    def reset(self):
        self.y = -self.h
        self.x = random.randint(0,W-self.w)
    def move(self):
        self.y += self.dy
        if self.y > H:
            self.y = -self.h
            self.x = random.randint(0,W-self.w)
    def chcoll(self,enemy):
        if enemy.x -self.w <= self.x <= enemy.x + enemy.w  and  enemy.y -self.h <= self.y <= enemy.y + enemy.h:
            self.y = -self.h
            self.x = random.randint(0,W-self.w)
            return True

        return False
    def draw(self,scr):
        self.im.set_colorkey((255,255,255))
        scr.blit(self.im,(self.x,self.y))
class Enemy():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.im = pg.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\2\\Enemy.png")
        self.rect = self.im.get_rect()
        self.w, self.h = self.rect[2], self.rect[3]
        self.dy = 10
    def move(self):
        self.y += self.dy
        global score
        if self.y > H:
            score += 1
            self.y = -self.h
            self.x = random.randint(0,W-self.w)
            self.dy += 1
    def draw(self,scr):
        self.im.set_colorkey((0,0,0))
        scr.blit(self.im,(self.x,self.y))
class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.im = pg.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\2\\Player.png")
        self.rect = self.im.get_rect()
        self.w, self.h = self.rect[2], self.rect[3]
        
    def move(self,dx):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] and self.x>0:
            self.x -= dx 
        if key[pg.K_RIGHT] and self.x<W - self.w - 10:
            self.x += dx
    def chcoll(self,enemy):
        if enemy.x -self.w <= self.x <= enemy.x + enemy.w  and  enemy.y -self.h <= self.y <= enemy.y + enemy.h:
            return True
        return False
    def draw(self,scr):
        self.im.set_colorkey((0,0,0))
        scr.blit(self.im,(self.x,self.y))
def main():
    cl = 0
    nn = 0
    global score 
    global coins
    run = True
    coin = Coin(W//2)
    enemy = Enemy(W//2,0)
    player = Player(W//2,H - 120)   
    dx = 15
    global over
    while run:
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN and over == 1:
                if (W//2 <= mouse[0] <= W//2 + 200) and (H//2 + 50<= mouse[1] <= H//2 + 100):
                    cl = 1
        if cl == 1:
            score = 0
            coins = 0
            enemy.dy = 10
            enemy.y = -enemy.h
            player.x = W//2
            over = 0
            nn = 0
        if over == 0:
            if coins == N or nn == N:
                enemy.dy += 5
            cl = 0
            tscore = my_font.render("Score: "+str(score), True, BLACK)
            tcoins = my_font.render("Coins: "+str(coins), True, BLACK)
            if player.chcoll(enemy):
                over = 1 
            if coin.chcoll(player):
                nn += 1
                coins += coin.weight
                coin.weight = random.randint(0,10)
            if coin.chcoll(enemy):
                coin.reset()
            scr.blit(Bg, (0,0)) 
            player.move(dx)
            player.draw(scr)
            enemy.move()
            coin.move()
            enemy.draw(scr)
            coin.draw(scr)
            scr.blit(tscore, (W-130,10)) 
            scr.blit(tcoins, (10,10)) 
        elif over == 1:
            scr.fill(BLACK)
            scr.blit(game_over, (W//2,H//2)) 
            scr.blit(NeW, (W//2,H//2 + 50))
        
        pg.display.flip()
        clock.tick(fps) 


if __name__ == '__main__':
    main()
