import pygame
# import os
# from tkinter import *
# import time
# from hangman import Hangman

# mängija = input("Palun sisestage oma nimi\n:").lower()

# time.sleep(1)

# uus_mäng = Hangman(arvamused="")

# uus_mäng.calc()

# _________________________________________________________

# Esialgne init
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")

# Button
RADIUS = 20
GAP = 15
tähed = []
algus_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
algus_y = 400
A = 65
for i in range(26):
    x = algus_x + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = algus_y + ((i // 13) * (GAP + RADIUS * 2))
    tähed.append([x, y, chr(A + i)])

# Font loomine
TÄHE_FONT = pygame.font.SysFont("comicsans", 35)


# Pildid
pildid = []
for i in range(7):
    pilt = pygame.image.load("Hangman" + str(i) + ".png")
    pildid.append(pilt)
print(pildid)

# Game variables

hangman_olek = 0

# värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)
    
    # Buttons
    for täht in tähed:
        x, y, täh = täht
        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
        text = TÄHE_FONT.render(täh, 1, BLACK)
        win.blit(text, (x - text.get_width()/ 2, y - text.get_height()/ 2))

    win.blit(pildid[hangman_olek], (100, 150))
    pygame.display.update()


while run == True:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
pygame.quit()