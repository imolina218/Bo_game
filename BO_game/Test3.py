import pygame
import os
import time
pygame.init()
pygame.font.init()

width, height = 680, 680
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bo game")

# Main variables
run = True
frame = 1
challenge = 0
cave = 1
lives = 4
score = 0
text = ''
user_text = ''
color_active = (255, 255, 255)
color_inactive = (0, 0, 0)

# Load images
frame_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),
                                         (width, height))
frame_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-black_LI.jpg")),
                                         (width, height))
frame_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-black_LI3.jpg")),
                                         (width, height))
frame_4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-black_LI3.jpg")),
                                         (width, height))
# Load fonts
main_font = pygame.font.SysFont("comicsans", 26)
riddle_font = pygame.font.SysFont("comicsans", 25)
title_font = pygame.font.SysFont("comicsans", 60)

# Riddles and answers
# Level 1
level_1 = ["You buy one dozen eggs. All but three break. How many eggs are left unbroken?", "If two’s company, and"
           " three’s a crowd, what are four and five?...", "What is the result of: 2 - 2 x 2 + 2 = ..."]
level_1_answers = ["three", "nine", "zero"]
# Level 2
level_2 = ["The more of this there is, the less you see. What is it?... ", "What five-letter word becomes shorter when "
           "you add two letters to it?...", "What is so fragile that saying its name breaks it?..."]
level_2_answers = ["darkness", "short", "silence"]
# Level 3
level_3 = ["In a feast everyone shook hands with everybody else. There were 66 handshakes.\n How many people were at"
           " the feast ?...", "I have lakes with no water, mountains with no stone and cities with no buildings. What"
           " am I?...", "What does man love more than life, hate more than death or mortal strife; that which contented"
           " men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to"
           " their graves?..."]
level_3_answers = ["twelve", "map", "nothing"]

def select_riddle(cave, challenge):
    while True:
        if cave == 1:
            display_challenge = level_1[challenge]
            break
        if cave == 2:
            display_challenge = level_2[challenge]
            break
        if cave == 3:
            display_challenge = level_3[challenge]
            break
    return display_challenge

def select_answer(cave, challenge):
    while True:
        if cave == 1:
            display_answer = level_1_answers[challenge]
            break
        if cave == 2:
            display_answer = level_1_answers[challenge]
            break
        if cave == 3:
            display_answer = level_1_answers[challenge]
            break
    return display_answer

def main_answer(cave, challenge, lives, run):
    while run:
        answer = select_answer(cave, challenge)
        user_answer = input("Enter your answer: ")
        if user_answer in answer:
            print("Correct!!")
            if challenge == 2:
                cave += 1
                challenge = 0
            else:
                challenge += 1
            if challenge == 3 and cave == 3:
                print("You Win the game.")
        else:
            lives -= 1

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

def img_adapt_f4f5f6(run, user_text):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        window.blit(frame_4, (0, 0))
        riddle_display = riddle_font.render(select_riddle(cave, challenge), 1, (255, 255, 255))
        user_text_disp = main_font.render(user_text, 1, (255, 255, 255))
        press_to_continue = title_font.render("Press ENTER to submit answer", 1, (255, 255, 255))
        window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
        window.blit(user_text_disp, (200, 300))
        window.blit(press_to_continue, (width - press_to_continue.get_width() - 20, 540))
        pygame.display.flip()


def main(run, frame, challenge, cave, lives, score, main_font, title_font, text, user_text, riddle_font):

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
        if frame == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and frame == 3:
                        img_adapt_f4f5f6(run, user_text)

        if frame == 4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and frame == 4:
                        # img_adapt_f4f5f6()
                        frame += 1
                        break
        if frame == 5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and frame == 5:
                        img_adapt_f1()
                        frame += 1
                        break




main(run, frame, challenge, cave, lives, score, main_font, title_font, text, user_text, riddle_font)






