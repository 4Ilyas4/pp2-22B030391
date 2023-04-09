import pygame
import os
from DATA import *
pygame.init()
pygame.display.set_caption("PainT_Ilyasa")
font = pygame.font.SysFont('Verdana', 11)
font1 = pygame.font.SysFont('Verdana', 20)
scr = pygame.display.set_mode((WIDTH,HEIGHT))
canv = pygame.Surface((WIDTH,HEIGHT-70)).convert_alpha()
scanv = pygame.Surface((500,200))
clock = pygame.time.Clock()
run = True

b1t = font.render("PEN", True, WHITE)
b2t = font.render("RECT", True, WHITE)
b3t = font.render("CIRC", True, WHITE)
b6t = font.render("SAVE", True, WHITE)
b7t = font.render("OPEN", True, WHITE)
b8t = font.render("CLOSE", True, WHITE)

class Button:
    def __init__(self,x,y,wid,hei,col,text = "1"):
        self.x = x
        self.y = y
        self.color = col
        self.wid = wid
        self.hei = hei
        self.text = text
        self.rect = pygame.Rect(self.x,self.y,self.wid,self.hei)
    def draw(self):
        pygame.draw.rect(scr,
                         self.color,
                         (self.x,self.y,self.wid,self.hei),
                         10
                         )
        pygame.draw.rect(scr,
                         WHITE,
                         (self.x,self.y,self.wid,self.hei),
                         1
                         )
        if self.text != "1":
            scr.blit(self.text, (self.x,self.y - 2))
class GameObject:
    def draw(self):
        return
    def update(self,width,color,current_pos):
        return
class Pen(GameObject):
    def __init__(self, *args, **kwargs): 
        self.points = []
        self.color = RED
        self.width = 1 
    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                canv,
                self.color,
                (point[0], point[1]), 
                (next_point[0], next_point[1]),
                self.width
            )
    def update(self,width,color,current_pos):
        self.points.append(current_pos)
        self.color = color
        self.width = width
class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_posx, self.start_posy  = start_pos
        self.end_posx, self.end_posy = start_pos
        self.color = RED
        self.width = 1 
    def draw(self):
        start_pos_x = min(self.start_posx, self.end_posx)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_posy, self.end_posy)
        end_pos_x = max(self.start_posx, self.end_posx)
        end_pos_y = max(self.start_posy, self.end_posy)
        pygame.draw.rect(
            canv,
            self.color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            self.width,
        )

    def update(self,width,color,current_pos):
        self.end_posx, self.end_posy = current_pos
        self.color = color
        self.width = width
class Circle(GameObject):
    def __init__(self, start_pos, *args, **kwargs):
        self.start_posx, self.start_posy = start_pos
        self.end_posx, self.end_posy = start_pos
        self.color = RED
        self.width = 1 
    def draw(self):

        r = ((self.end_posx-self.start_posx)**2+(self.end_posy-self.start_posy)**2)**0.5
        pygame.draw.circle(
            canv,
            self.color,
            (self.start_posx,self.start_posy),
            r,
            self.width
        )

    def update(self,width,color,current_pos):
        self.end_posx, self.end_posy = current_pos
        self.color = color
        self.width = width

load = False
save = False
i = 0
j = 0

b16 = Button(240,20,37,10,DARKGRN,b6t)
b17 = Button(240,35,37,10,DARKGRN,b7t)
b18 = Button(240,50,37,10,RED,b8t)

b1 = Button(20,20,27,10,DARKGRN,b1t)
b2 = Button(20,50,27,10,DARKGRN,b2t)
b3 = Button(20,35,27,10,DARKGRN,b3t)

b4 = Button(60,20,27,10,RED)
b5 = Button(60,35,27,10,ORANGE)
b6 = Button(60,50,27,10,YELLOW)

b7 = Button(100,20,27,10,GREEN)
b8 = Button(100,35,27,10,BBLUE)
b9 = Button(100,50,27,10,BLUE)

drawload = False
savename = ""
filename = ""
file_dir = "C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\3\\Images"
files_list = os.listdir(file_dir)
widt = 1
colo = RED

game_object = GameObject()
active_obj = game_object
current_shape = Pen  # current_shape()
objects = []

while run:
    scr.fill(BLACK)
    scr.blit(canv,(0,70))   
    canv.fill(WHITE)
    if drawload:
        canv.blit(imag, (0,0)) 
    scanv.fill(GREY)
    if save:
        tx = 50
        ty = (scanv.get_height()//2) - 15
        tw = 400
        tt = font1.render("Сохранить как", True, (255, 0, 0))
        ts = font1.render(filename, True, (255, 0, 0))
        th = ts.get_height() +10
        pygame.draw.rect(scanv,
                         BLACK,
                         (tx,ty,tw,th),
                         1
                         )
        scanv.blit(ts, ts.get_rect(center = scanv.get_rect().center)) 
        scanv.blit(tt, (40 , 34))  
        scr.blit(scanv,(200,200))

    elif load:  
        tx = 50
        ty = (scanv.get_height()//2) - 15
        tw = 400
        tt = font1.render("Введите название файла без формата", True, (255, 0, 0))
        ts = font1.render(filename, True, (255, 0, 0))
        th = ts.get_height() +10
        pygame.draw.rect(scanv,
                         BLACK,
                         (tx,ty,tw,th),
                         1
                         )
        scanv.blit(ts, ts.get_rect(center = scanv.get_rect().center)) 
        scanv.blit(tt, (40 , 34))  
        scr.blit(scanv,(200,200))
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b16.draw()
    b17.draw()
    b18.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b18.rect.collidepoint(event.pos):
                run = False
            if b1.rect.collidepoint(event.pos):
                current_shape = Pen
            if b2.rect.collidepoint(event.pos):
                current_shape = Rectangle
            if b3.rect.collidepoint(event.pos):
                current_shape = Circle
            if b16.rect.collidepoint(event.pos):
                save = True
            if b17.rect.collidepoint(event.pos):
                load = True
            if b4.rect.collidepoint(event.pos):
                colo = RED
            if b5.rect.collidepoint(event.pos):
                colo = ORANGE
            if b6.rect.collidepoint(event.pos):
                colo = YELLOW
            if b7.rect.collidepoint(event.pos):
                colo = GREEN
            if b8.rect.collidepoint(event.pos):
                colo = BBLUE
            if b9.rect.collidepoint(event.pos):
                colo = BLUE
            else:
                active_obj = current_shape(start_pos=(event.pos[0],event.pos[1]-70))
                objects.append(active_obj)
        if event.type == pygame.MOUSEMOTION:
            curp = (event.pos[0],event.pos[1]-70)
            active_obj.update(widt,colo,curp)
        if event.type == pygame.MOUSEBUTTONUP:
            active_obj = game_object
        if event.type == pygame.KEYDOWN and (load or save):
                if event.key == pygame.K_RETURN:
                    if load and not save:
                        i = 1 
                    elif save and not load:
                        j = 1
                    load = False
                    save = False
                elif event.key == pygame.K_BACKSPACE:
                    filename =  filename[:-1]
                else:
                    filename += event.unicode
        if event.type == pygame.MOUSEWHEEL:
                widt += event.y   
    for obj in objects:
        obj.draw()
    if i == 1:
        try:
            imag = pygame.image.load("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\3\\Images\\"+str(filename)+".png")
            drawload = True
        except FileNotFoundError: 
            drawload = False  
        i = 0
    if j == 1:
        pygame.image.save(canv, "C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis8\\3\\Images\\"+str(filename)+".png")
        j = 0  
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()