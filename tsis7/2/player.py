import pygame as pg
import sys
import os
pg.init()
music_dir = "music/"
music_files = os.listdir(music_dir)
l = len(music_files)
def play_music(fl):
    pg.mixer.music.load(fl)
    pg.mixer.music.play()
def display_music_list():
    font = pg.font.Font(None, 30)
    for i, file in enumerate(music_files):
        text = font.render(str(i+1) + ". " + file, True, (255, 255, 255))
        win.blit(text, (10, i*30 + 10))

FPS = 60
W = 700  
H = 300 
k = 1
i = 0
win  = pg.display.set_mode((W, H))
clock = pg.time.Clock()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run= False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run= False
            elif event.key == pg.K_p:
                play_music(os.path.join(music_dir, music_files[i]))
            elif event.key == pg.K_SPACE:
                k += 1
                if k%2==0:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_w:
                if i<l-1:
                    i += 1 
                    pg.mixer.music.stop()
                    play_music(os.path.join(music_dir, music_files[i]))
                else:
                    i = 0
                    pg.mixer.music.stop()
                    play_music(os.path.join(music_dir, music_files[i]))
                    
            elif event.key == pg.K_s:
                if i>=0:
                    i -= 1 
                    pg.mixer.music.stop()
                    play_music(os.path.join(music_dir, music_files[i]))
                else:
                    i = l-1
                    pg.mixer.music.stop()
                    play_music(os.path.join(music_dir, music_files[i]))
    win.fill((0, 0, 0))
    display_music_list()
    pg.display.update()
    clock.tick(FPS)

pg.quit()
 
