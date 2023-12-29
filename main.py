import os, sys
import pygame
from pygame.constants import KEYDOWN, KEYUP, K_b, K_c, K_d, K_g, K_h, K_j, K_m, K_n, K_s, K_v, K_x, K_z
from pygame.rect import Rect

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#variables and constants
HEIGHT = 200
WIDTH = 510
#colors
BLACK = (0, 0, 0)
BLACK1 = (0, 0, 0)
BLACK2 = (0, 0, 0)
BLACK3 = (0, 0, 0)
BLACK4 = (0, 0, 0)
BLACK5 = (0, 0, 0)
WHITE = (192,192,192)
RED = (255,50,53)
YELLOW = (255,255,0)
ORANGE = (255, 128, 37)
GREEN = (33,238,45)
BLUE = (98,172,255)
INDIGO = (33,79,255)
VIOLET = (167,38,255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PIANO PLAYER")

#variables for drawing
key_1 = pygame.Rect(20, 50, 50, 150)
Key_2 = pygame.Rect(90, 50, 50, 150)
Key_3 = pygame.Rect(160, 50, 50, 150)
Key_4 = pygame.Rect(230, 50, 50, 150)
Key_5 = pygame.Rect(300, 50, 50, 150)
Key_6 = pygame.Rect(370, 50, 50, 150)
Key_7 = pygame.Rect(440, 50, 50, 150)
Key_8 = pygame.Rect(55, 50, 50, 75)
Key_9 = pygame.Rect(125, 50, 50, 75)
Key_10 = pygame.Rect(265, 50, 50, 75)
Key_11 = pygame.Rect(335, 50, 50, 75)
Key_12 = pygame.Rect(405, 50, 50, 75)

#Font Variables
game_font = pygame.font.Font("./font/Roboto-Black.ttf", 32)

#sounds variables
c = pygame.mixer.Sound("./sound/C.wav")
c_sharp = pygame.mixer.Sound("./sound/C_s.wav")
d = pygame.mixer.Sound("./sound/D.wav")
d_sharp = pygame.mixer.Sound("./sound/D_s.wav")
e = pygame.mixer.Sound("./sound/E.wav")
f = pygame.mixer.Sound("./sound/F.wav")
f_sharp = pygame.mixer.Sound("./sound/F_s.wav")
g = pygame.mixer.Sound("./sound/G.wav")
g_sharp = pygame.mixer.Sound("./sound/G_s.wav")
a = pygame.mixer.Sound("./sound/A.wav")
a_sharp = pygame.mixer.Sound("./sound/Bb.wav")
b = pygame.mixer.Sound("./sound/B.wav")

#Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_z:
                c.play()
                RED = (128,0,0)

            if event.key == K_x:
                d.play()
                ORANGE = (210, 121, 23)
                
            if event.key == K_c:
                e.play()
                YELLOW = (128,128,0)
                
            if event.key == K_v:
                f.play()
                GREEN = (0,128,0)
                
            if event.key == K_b:
                g.play()
                BLUE = (0,128,128)
                
            if event.key == K_n:
                a.play()
                INDIGO = (0,0,128)
                
            if event.key == K_m:
                b.play()
                VIOLET = (113,0,96)

            if event.key == K_s:
                c_sharp.play()
                BLACK1 = (128,128,128)

            if event.key == K_d:
                d_sharp.play()
                BLACK2 = (128,128,128)


            if event.key == K_g:
                f_sharp.play()
                BLACK3 = (128,128,128)


            if event.key == K_h:
                g_sharp.play()
                BLACK4 = (128,128,128)


            if event.key == K_j:
                a_sharp.play()
                BLACK5 = (128,128,128)

            

        #ON KEYUP 
        if event.type == KEYUP:
            if event.key == K_z:
                RED = (255,50,53)

            if event.key == K_x:
                ORANGE = (255, 128, 37)
                
            if event.key == K_c:
                YELLOW = (255,255,0)
                
            if event.key == K_v:
                GREEN = (33,238,45)
                
            if event.key == K_b:
                BLUE = (98,172,255)
                
            if event.key == K_n:
                INDIGO = (33,79,255)
                
            if event.key == K_m:
                VIOLET = (167,38,255)

            if event.key == K_s:
                BLACK1 = (0, 0, 0)

            if event.key == K_d:
                BLACK2 = (0, 0, 0)

            if event.key == K_g:
                BLACK3 = (0, 0, 0)

            if event.key == K_h:
                BLACK4 = (0, 0, 0)

            if event.key == K_j:
                BLACK5 = (0, 0, 0)


        #Screen Display        
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, key_1)
        pygame.draw.rect(screen, ORANGE, Key_2)
        pygame.draw.rect(screen, YELLOW, Key_3)
        pygame.draw.rect(screen, GREEN, Key_4)
        pygame.draw.rect(screen, BLUE, Key_5)
        pygame.draw.rect(screen, INDIGO, Key_6)
        pygame.draw.rect(screen, VIOLET, Key_7)
        pygame.draw.rect(screen, BLACK1, Key_8)
        pygame.draw.rect(screen, BLACK2, Key_9)
        pygame.draw.rect(screen, BLACK3, Key_10)
        pygame.draw.rect(screen, BLACK4, Key_11)
        pygame.draw.rect(screen, BLACK5, Key_12)
        welcome_text = game_font.render(f"WELOME TO PIANO PLAYER", False, BLACK)
        screen.blit(welcome_text, (50, 10))


    pygame.display.flip()
    pygame.display.update()