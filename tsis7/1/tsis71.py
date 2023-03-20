import pygame as pg
import time
lt = time.localtime()
ats = int(time.strftime("%S", lt))
atm =int(time.strftime("%M", lt))

def lit(im,rect):
    im.set_colorkey((0,0,0))
    screen.blit(im,rect)
def rotate(surface, angle, pivot, ofs):
    r_im = pg.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    r_ofs= ofs.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = r_im.get_rect(center=pivot+r_ofs)
    return r_im, rect  # Return the rotated image and shifted rect.

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
pivot = [400, 400]
pivot1 = [400, 400]
ofs = pg.math.Vector2((-195//2)+21, (-165//2)+21)
ofs1 = pg.math.Vector2((-251//2)+21, (-168//2)+21)
angle = 0+30*atm+54
angle1 = 3+6*ats+48
bgim = pg.image.load("mickeyclock.jpg")
im = pg.image.load("lh.png").convert_alpha()
im1 = pg.image.load("rh.png").convert_alpha()#
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    angle += 1/10
    r_im, rect = rotate(im, angle, pivot, ofs)
    angle1 += 6 
    r_im1, rect1 = rotate(im1, angle1, pivot1, ofs1)
    screen.blit(bgim,(0,0))
    lit(r_im,rect)
    lit(r_im1,rect1)
    pg.display.update()
    clock.tick(1)
   
pg.quit()

