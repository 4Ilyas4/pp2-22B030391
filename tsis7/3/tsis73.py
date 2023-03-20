import pygame as pg
RED = (255,0,0)
fps = 60
W=800
H=800
pg.init()
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
x, y = 400, 400
k = 20
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    key = pg.key.get_pressed()
    if key[pg.K_ESCAPE]:
        run= False
    if key[pg.K_UP] and y>25:
        y -= k
    if key[pg.K_DOWN] and y<H-25-5:
        y += k
    if key[pg.K_LEFT] and x>25 :
        x -= k
    if key[pg.K_RIGHT] and x<W-25-5:
        x += k
 
    screen.fill((255,255,255))
    
    pg.draw.circle(screen, RED,(x,y),25)

    
    pg.display.update()
    clock.tick(fps)
   
pg.quit()
