import random
import pygame

pygame.init() # инициализация библиотеки pygame 
WIDTH, HEIGHT = 800, 800 # начальные данные
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0) # цвета
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 50 # размер блока , пикселя
WHITE = (255, 255, 255)
RGR = (50,200,10)
clock = pygame.time.Clock() # создание зарержки в игре те времени
my_font = pygame.font.SysFont('Comic Sans MS', 30) # для текста

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RGR,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y

        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x >= WIDTH // BLOCK_SIZE:
            self.body[0].x = 0 
         
       
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        
        
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        
        
        elif self.body[0].y >= HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0
      
          
      
    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    def check_selfcol(self):
        for i in range(len(self.body) - 1, 1, -1):
            if self.body[i].x == self.body[0].x and self.body[i].y == self.body[0].y:
                return True
        return False

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


def main():
    running = True 
    snake = Snake()  # создание змеи
    food = Food(5, 5)  # создание еды
    dx, dy = 0, 0 # начальные данные в игре
    score  = 0 
    level = 0
    Ug = 1
    Rg = 1
    T = 5
    over = 0
    cl = 0
    while running:
        SCREEN.fill(BLACK)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get(): # обработка событии
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and over == 1:
                if (WIDTH//2 -100 <= mouse[0] <= WIDTH//2 + 100) and (HEIGHT//2 <= mouse[1] <= HEIGHT//2 + 100):
                    cl = 1
            
            if event.type == pygame.KEYDOWN:  # изменение скорости при нажатии на кнопки
                if event.key == pygame.K_UP and Rg == 1 :#я добавил Rg Ug для того чтобы когда ты к примеру идешь в перед потом назад то ты не сталкивался сам с собой и дальше двигался в перед
                    dx, dy = 0, -1
                    Ug = 1
                    Rg = 0
                elif event.key == pygame.K_DOWN and Rg == 1 :
                    dx, dy = 0, +1
                    Ug = 1
                    Rg = 0
                elif event.key == pygame.K_RIGHT and Ug == 1 :
                    dx, dy = 1, 0
                    Rg = 1
                    Ug = 0
                elif event.key == pygame.K_LEFT and Ug == 1 :
                    dx, dy = -1, 0
                    Rg = 1
                    Ug = 0
        
        if cl == 1:
            dx, dy = 0, 0 # начальные данные в игре
            score  = 0 
            level = 0
            Ug = 1
            Rg = 1
            T = 5
            snake.body.clear()
            snake.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            ]

            over = 0
        if over == 0: #
            cl = 0
            snake.move(dx, dy)  # вызов функции движения змеи
            if snake.check_collision(food):  # функция столкновения с едой
                score += 1  # увеличение очков при столкновении с едой
                if score %3 == 0:
                    T += 1  # увеличение скорости игры в случае увеличения очков на 3
                    level +=1  # увеличение уровня в случае увеличеня очков на 3
                    snake.body.append(      
                        Point(snake.body[-1].x, snake.body[-1].y)  # удлиннение змеи 
                    ) 

                food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)   # изменение позиции еды на рандоомные и в следующем кадре он будет отрисован на других коорд
                food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1) 
            if snake.check_selfcol():  # закрытие игры в случае столкновеня с собой
                over = 1
            snake.draw()# вывод функции для отрисовки змеи
            food.draw() # вывод функции для отрисовки еды
            draw_grid() # вывод функции для отрисовки фона
            text_score = my_font.render('Score :'+str(score), False, (0, 255, 0))
            SCREEN.blit(text_score, (20,20)) #вывод на экран очков
            text_level = my_font.render('Level :'+str(level), False, (0, 255, 0))
            SCREEN.blit(text_level, (WIDTH - 300,20))# вывод на экран уровня     
        elif over == 1:
            text_over = my_font.render('Game Over', False, (250, 0, 0))
            SCREEN.blit(text_over, (WIDTH//2 -100,HEIGHT//2 -100)) #вывод на экран очков
            text_over = my_font.render('New Game', False, (250, 250, 0))
            SCREEN.blit(text_over, (WIDTH//2 -100,HEIGHT//2)) #вывод на экран очков
        pygame.display.flip() # обновление экрана
        clock.tick(T)  # управление временем через Т


if __name__ == '__main__':
    main()