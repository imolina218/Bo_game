import pygame
import os
from time import sleep

pygame.font.init()

width, height = 680, 680
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bo game")

# Load images
frame1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),
                                (width, height))
frame2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-black_LI.jpg")),
                                (width, height))
frame3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-black_LI3.jpg")),
                                (width, height))


def main():
    run = True
    level = 0
    lives = 4
    score = 0
    raghnak = True
    lordk = True
    usarkna = True
    main_font = pygame.font.SysFont("comicsans", 30)
    title_font = pygame.font.SysFont("comicsans", 60)
    text = ''
    user_text = ''

    def img_adapt_f1():
        window.blit(frame1, (0, 0))
        # apply text
        press_to_continue = title_font.render("Press ENTER to start", 1, (255, 255, 255))

        window.blit(press_to_continue, (height - press_to_continue.get_height() - 510, 600))

        pygame.display.update()

    def img_adapt_f2():
        window.blit(frame2, (0, 0))
        # apply text
        press_to_continue = title_font.render("Press ENTER to continue", 1, (255, 255, 255))

        window.blit(press_to_continue, (height - press_to_continue.get_height() - 560, 600))

        pygame.display.update()

    def img_adapt_f3():
        window.blit(frame3, (0, 0))
        # apply text
        press_to_continue = title_font.render("Press ENTER to continue", 1, (255, 255, 255))

        window.blit(press_to_continue, (height - press_to_continue.get_height() - 560, 600))

        pygame.display.update()

    def img_adapt_f4():
        window.blit(frame3, (0, 0))
        # apply text
        press_to_continue = title_font.render("Press ENTER to continue", 1, (255, 255, 255))

        window.blit(press_to_continue, (height - press_to_continue.get_height() - 560, 600))

        pygame.display.update()

    def img_adapt_f5():
        window.blit(frame3, (0, 0))
        # apply text
        press_to_continue = title_font.render("Press ENTER to continue", 1, (255, 255, 255))

        window.blit(press_to_continue, (height - press_to_continue.get_height() - 560, 600))

        pygame.display.update()

    def img_adapt_f6():
        window.blit(frame3, (0, 0))
        # apply text
        press_to_continue = title_font.render("Press ENTER to continue", 1, (255, 255, 255))

        window.blit(press_to_continue, (height - press_to_continue.get_height() - 560, 600))

        pygame.display.update()

    def img_adapt_f7():
        window.blit(frame3, (0, 0))
        # apply text
        press_to_continue = title_font.render("Press ENTER to continue", 1, (255, 255, 255))

        window.blit(press_to_continue, (height - press_to_continue.get_height() - 560, 600))

        pygame.display.update()

    while run:
        img_adapt_f1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sleep(1.5)
                    while run:
                        img_adapt_f2()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sleep(1.5)
                                    while run:
                                        img_adapt_f3()
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                run = False




main()
