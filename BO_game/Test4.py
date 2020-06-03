import pygame
import os
import time
pygame.init()
pygame.font.init()

width, height = 680, 680
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bo game")

# Load images
frame_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),
                                         (width, height))
frame_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-black_LI.jpg")),
                                         (width, height))
frame_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-black_LI3.jpg")),
                                         (width, height))
# Load fonts
main_font = pygame.font.SysFont("comicsans", 26)
title_font = pygame.font.SysFont("comicsans", 60)

def img_adapt_f1():
    window.blit(frame_1, (0, 0))
    # apply text
    press_to_continue = title_font.render("Press ENTER to start", 1, (255, 255, 255))
    window.blit(press_to_continue, (width - press_to_continue.get_width() - 130, 540))
    pygame.display.update()

def img_adapt_f2():
    window.blit(frame_2, (0, 0))
    # apply text
    press_to_continue = title_font.render("Press ENTER to continue", 1, (255, 255, 255))
    rules = title_font.render("Rules:", 1, (255, 255, 255))
    r1 = main_font.render(" You have to challenge 3 viking creatures.", 1, (255, 255, 255))
    r2 = main_font.render(" Each creature wil give you 3 riddles.", 1, (255, 255, 255))
    r3 = main_font.render(" Eight lives are given to you.", 1, (255, 255, 255))
    r4 = main_font.render(" Each riddle you get wrong, a live less.", 1, (255, 255, 255))
    r5 = main_font.render(" If you ran out of lives, you loose.", 1, (255, 255, 255))
    r6 = main_font.render(" If you loose a restart game option wil appear", 1, (255, 255, 255))

    window.blit(rules, (width - rules.get_width() - 280, 50))
    pygame.display.update()
    time.sleep(2)
    window.blit(r1, (width - r1.get_width() - 180, 140))
    window.blit(r2, (width - r2.get_width() - 200, 200))
    window.blit(r3, (width - r3.get_width() - 240, 260))
    window.blit(r4, (width - r4.get_width() - 190, 320))
    window.blit(r5, (width - r5.get_width() - 210, 380))
    window.blit(r6, (width - r6.get_width() - 170, 440))
    pygame.display.update()
    time.sleep(10)
    window.blit(press_to_continue, (width - press_to_continue.get_width() - 90, 540))
    pygame.display.update()

def img_adapt_f3():
    window.blit(frame_3, (0, 0))
    # apply text
    press_to_continue = title_font.render("Press ENTER to start", 1, (255, 255, 255))

    window.blit(press_to_continue, (width - press_to_continue.get_width() - 130, 540))

    pygame.display.update()


def main():
    run = True
    frame = 1
    challenge = 0
    cave = 0
    lives = 4
    score = 0
    main_font = pygame.font.SysFont("comicsans", 30)
    title_font = pygame.font.SysFont("comicsans", 60)
    text = ''
    user_text = ''

    img_adapt_f1()
    while run:
        if frame == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and frame == 1:
                        img_adapt_f2()
                        frame += 1
                        break
        if frame == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and frame == 2:
                        img_adapt_f3()
                        frame += 1
                        break






main()
