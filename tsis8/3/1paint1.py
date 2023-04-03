import pygame

pygame.init() #инициализация pygame
               #начальные данные
WIDTH = 800   
HEIGHT = 800
color=(255,255,0)#начальный цвет

drawmode = 'line'#начальный режим рисования

radius=10#начальный радиус карандаша

running = True
drawing = False

FPS = 1000

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))#изначальный фон, если бы он был в цикле то было бы обычное движение шарика или просто появление и исчезновение прямоугольника или круга

p = []#создание массива в котором элементами будут координаты курсора

def draw_rect(screen,color, p):
    if len(p)>1:# чтобы не вылетало если массив еще не заполнен
        px = p[0][0]#начальные координаты когда пользователь нажал на кнопку мышки
        py = p[0][1]
        plx = p[len(p)-1][0] #конечные
        ply = p[len(p)-1][1]
        pygame.draw.rect(screen,color,(px,py,plx - px,ply - py))

def draw_circ(screen,color,p):
    if len(p)>1:
        px = p[0][0]#same
        py = p[0][1]
        plx = p[len(p)-1][0]
        ply = p[len(p)-1][1]
        r = ((plx - px)**2+(ply - py)**2)**0.5
        pygame.draw.circle(screen,color,(px,py),r)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            if drawmode == 'rct': # отображение прямоугольника после того как пользователь отпустил кнопку мыши 
                draw_rect(screen,color,p)
            elif drawmode == 'circ': # отображение круга после того как пользователь отпустил кнопку мыши 
                draw_circ(screen,color,p)
            p = []#отчищение массива курсора для новой фигуры (с нового места)
        elif event.type == pygame.MOUSEMOTION and drawing:
            p.append(event.pos) # пополнение массива о положении курсора во время нажатия 
            if drawmode == 'line':
                pygame.draw.circle(screen, color, event.pos , radius)
        elif event.type == pygame.KEYDOWN:#изменение режимов рисования на: круг прямоугольник и карандаш
            if  event.key == pygame.K_n:
                drawmode = 'line'
            elif event.key == pygame.K_r:
                drawmode = 'rct'
            elif event.key == pygame.K_l:
                drawmode = 'circ'

        if event.type == pygame.MOUSEWHEEL: # изменение радиуса карандаша
                radius += event.y 
        pressed = pygame.key.get_pressed()   #изменение цвета рисования 1-черный 2-красный 3-зеленый 4-синий 5-желтый 6-белый тоесть ластик
        if pressed[pygame.K_0]: 
            screen.fill((255,255,255)) #отчистить все
        if pressed[pygame.K_1]: 
            color = ((0,0,0))
        if pressed[pygame.K_2]: 
            color = ((255,0,0))
        if pressed[pygame.K_3]: 
            color = ((0,255,0))
        if pressed[pygame.K_4]: 
            color = ((0,0,255))
        if pressed[pygame.K_5]:
            color = ((255,255,0))
        if pressed[pygame.K_6]: 
            color = ((255, 255, 255))#ластик
        clock.tick(FPS)
    pygame.display.flip()#обновление экрана
pygame.quit()