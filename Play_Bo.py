import pygame
import os
import time
import random

pygame.init()

width, height = 680, 680
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bo game")
clock = pygame.time.Clock()
pygame.mixer.music.load(os.path.join('assets', 'VIKINGS Most Epic Viking & Nordic Folk Music Danheim.mp3'))
pygame.mixer.music.play(3)

# Load images
frame_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "img_frame01.png")), (width, height))
frame_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "img_frame02.png")), (width, height))
frame_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "img_frame03.png")), (width, height))
frame_4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Enemy01.png")), (width, height))
frame_5 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Enemy02.png")), (width, height))
frame_6 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Enemy03.png")), (width, height))
frame_7 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Enemy04.png")), (width, height))
frame_8 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Enemy05.png")), (width, height))

walk01_frame = pygame.transform.scale(pygame.image.load(os.path.join("assets", "img_walk01.png")), (width, height))
walk02_frame = pygame.transform.scale(pygame.image.load(os.path.join("assets", "img_walk02.png")), (width, height))
frame_lost = pygame.transform.scale(pygame.image.load(os.path.join("assets", "img_frame01.png")), (width, height))

# Load fonts
main_font = pygame.font.SysFont("comicsans", 26)
riddle_font = pygame.font.SysFont("comicsans", 25)
title_font = pygame.font.SysFont("comicsans", 60)

# Riddles and answers
# Level 1
level_1 = ["You buy one dozen eggs. All but three break. How many eggs are left unbroken?", "If two’s company, and"
           " three’s a crowd, what are four and five?...            ",
           "What is the result of: 2 - 2 x 2 + 2 = ...                                  "]
level_1_answers = ["three", "nine", "zero"]
# Level 2
level_2 = ["The more of this there is, the less you see. What is it?...                ",
           "What five-letter word becomes shorter when you add two letters to it?...     ",
           "What is so fragile that saying its name breaks it?...                      "]
level_2_answers = ["darkness", "short", "silence"]
# Level 3
level_3 = ["I have cities, but no houses. I have mountains, but no trees. What am I?...   ",
           "Where can you finish a book without finishing a sentence?...                   ",
           "What flies without wings?...                                          "]
level_3_answers = ["map", "prison", "time"]
# Level 3
level_4 = ["What must be broken before it can be used?...                         ",
           "What's strong enough to smash ships but still fears the sun?...           ",
           "I am the son of water but if water touches me i die, what am i?...         "]
level_4_answers = ["eggs", "ice", "salt"]
# Level 3
level_5 = ["I go up and down, sometimes i am curvy or straight, what am i?...     ",
           "I can fill a room or just one heart. Others may have me but cannot shared...",
           "What's nowhere but everywhere, except where something is, what am i?..."]
level_5_answers = ["stairs", "loneliness", "nothing"]

# Responses
# Correct
correct_list = ["Well done!", "well trained!", "Hmm correct!", "Seems right!", "Next one!", "Another one!", "Good brain"]
# Wrong
wrong_list = ["Hmmm wrong!", "Try harder!", "Not right!", "Seems wrong!", "Bad brain!", "Try again!", "Hmm naa"]


def select_riddle(cave, challenge):
    while True:
        if cave == 1:
            display_challenge = level_1[challenge]
            break
        elif cave == 2:
            display_challenge = level_2[challenge]
            break
        elif cave == 3:
            display_challenge = level_3[challenge]
            break
        elif cave == 4:
            display_challenge = level_4[challenge]
            break
        elif cave == 5:
            display_challenge = level_5[challenge]
            break
    return display_challenge


def select_answer(cave, challenge):
    while True:
        if cave == 1:
            display_answer = level_1_answers[challenge]
            break
        elif cave == 2:
            display_answer = level_2_answers[challenge]
            break
        elif cave == 3:
            display_answer = level_3_answers[challenge]
            break
        elif cave == 4:
            display_answer = level_4_answers[challenge]
            break
        elif cave == 5:
            display_answer = level_5_answers[challenge]
            break
    return display_answer


def monster_transition(cave):
    for print_frame in range(0, 700, 10):
        window.blit(walk01_frame, (0, 0), (680 - print_frame, 0, 50 + print_frame, 680))
        pygame.display.update()
        clock.tick(50)

    textLevelStart = title_font.render("Level " + str(cave), True, (255, 255, 255))
    window.blit(textLevelStart, [280, 340])
    pygame.display.update()
    clock.tick(1)

    for print_frame in range(0, 700, 10):
        window.blit(walk02_frame, (0, 0), (680 - print_frame, 0, 50 + print_frame, 680))
        pygame.display.update()
        clock.tick(50)


def music_play():
    pygame.event.poll()
    clock.tick(10)


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
    r1 = main_font.render(" You have to challenge 5 viking Gods.", 1, (255, 255, 255))
    r2 = main_font.render(" Each creature wil give you 3 riddles.", 1, (255, 255, 255))
    r3 = main_font.render(" Eight lives are given to you.", 1, (255, 255, 255))
    r4 = main_font.render(" Each riddle you get wrong, one live less.", 1, (255, 255, 255))
    r5 = main_font.render(" If you ran out of lives, you loose.", 1, (255, 255, 255))
    r6 = main_font.render(" If you loose a restart game option wil appear", 1, (255, 255, 255))
    r7 = main_font.render(" The answer is always one word", 1, (255, 255, 255))

    window.blit(rules, (width - rules.get_width() - 280, 50))
    pygame.display.update()
    time.sleep(2)
    window.blit(r1, (width - r1.get_width() - 180, 140))
    window.blit(r2, (width - r2.get_width() - 200, 200))
    window.blit(r3, (width - r3.get_width() - 240, 260))
    window.blit(r4, (width - r4.get_width() - 190, 320))
    window.blit(r5, (width - r5.get_width() - 210, 380))
    window.blit(r6, (width - r6.get_width() - 170, 440))
    window.blit(r7, (width - r3.get_width() - 240, 500))
    pygame.display.update()
    time.sleep(10)
    window.blit(press_to_continue, (width - press_to_continue.get_width() - 90, 540))
    pygame.display.update()


def img_adapt_f3():
    window.blit(frame_3, (0, 0))
    # apply text
    press_to_continue = title_font.render("Press ENTER to start", 1, (255, 255, 255))
    h1 = main_font.render(" You wil be Bo a viking warrior,", 1, (255, 255, 255))
    h2 = main_font.render(" this time the only muscle that apply", 1, (255, 255, 255))
    h3 = main_font.render(" to win the war is the brain and intellect.", 1, (255, 255, 255))
    h4 = main_font.render(" The faith of the people is with you so that", 1, (255, 255, 255))
    h5 = main_font.render(" you can prove the intellect of the vikings, ", 1, (255, 255, 255))
    h6 = main_font.render(" and more years of fortune will belong", 1, (255, 255, 255))
    h7 = main_font.render(" to the viking people for the great conquest.", 1, (255, 255, 255))
    h8 = main_font.render(" The difficulty is progresive.", 1, (255, 255, 255))
    h9 = main_font.render(" GOOD LUCK", 1, (255, 255, 255))

    window.blit(h1, (width - h1.get_width() - 220, 140))
    window.blit(h2, (width - h2.get_width() - 200, 180))
    window.blit(h3, (width - h3.get_width() - 200, 220))
    window.blit(h4, (width - h4.get_width() - 170, 260))
    window.blit(h5, (width - h5.get_width() - 180, 300))
    window.blit(h6, (width - h6.get_width() - 180, 340))
    window.blit(h7, (width - h7.get_width() - 150, 380))
    window.blit(h8, (width - h8.get_width() - 240, 420))
    window.blit(h9, (width - h9.get_width() - 180, 460))

    window.blit(press_to_continue, (width - press_to_continue.get_width() - 130, 540))

    pygame.display.update()


def main():
    run = True
    frame = 1
    challenge = 0
    cave = 1
    lives = 8
    user_input = ''

    img_adapt_f1()
    while run:
        music_play()
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
                    monster_transition(cave)
                    time.sleep(1)
                    window.blit(frame_4, (0, 0))
                    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                    riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                        (255, 255, 255))
                    press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                          (255, 255, 255))
                    window.blit(lives_label, (20, 15))
                    window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                    window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                    pygame.display.update()
                    if event.key == pygame.K_RETURN and frame == 3:
                        while frame == 3:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_BACKSPACE:
                                        user_input = user_input[:-1]
                                    else:
                                        user_input += event.unicode
                                    if event.key == pygame.K_RETURN:
                                        answer = select_answer(cave, challenge)
                                        user_answer = user_input[:-1]
                                        user_answer = user_answer.lower()
                                        if user_answer == answer:
                                            user_text = main_font.render(random.choice(correct_list), 1, (255, 255, 255))
                                            window.blit(user_text, (300, 450))
                                            pygame.display.update()
                                            if challenge == 2:
                                                cave += 1
                                                challenge = 0
                                                frame += 1
                                                user_input = ''
                                                break
                                            else:
                                                challenge += 1
                                                user_input = ''
                                            time.sleep(1)
                                        else:
                                            if lives == 0:
                                                frame = 9
                                                break
                                            else:
                                                lives -= 1
                                                user_text = main_font.render(random.choice(wrong_list), 1, (255, 255, 255))
                                                window.blit(user_text, (300, 450))
                                                pygame.display.update()
                                                time.sleep(4)
                                                user_input = ''
                                window.blit(frame_4, (0, 0))
                                lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                                user_text = main_font.render(user_input, 1, (255, 255, 255))
                                riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                                    (255, 255, 255))
                                press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                                      (255, 255, 255))
                                text_line = main_font.render("______"*8, 1, (255, 255, 255))
                                window.blit(lives_label, (20, 15))
                                window.blit(user_text, (320, 420))
                                window.blit(text_line, (120, 425))
                                window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                                window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                                pygame.display.update()
        if frame == 4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    monster_transition(cave)
                    time.sleep(1)
                    window.blit(frame_5, (0, 0))
                    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                    riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                        (255, 255, 255))
                    press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                          (255, 255, 255))
                    window.blit(lives_label, (20, 15))
                    window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                    window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                    pygame.display.update()
                    if event.key == pygame.K_RETURN and frame == 4:
                        while frame == 4:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_BACKSPACE:
                                        user_input = user_input[:-1]
                                    else:
                                        user_input += event.unicode
                                    if event.key == pygame.K_RETURN:
                                        answer = select_answer(cave, challenge)
                                        user_answer = user_input[:-1]
                                        user_answer = user_answer.lower()
                                        if user_answer == answer:
                                            user_text = main_font.render(random.choice(correct_list), 1,
                                                                         (255, 255, 255))
                                            window.blit(user_text, (300, 450))
                                            pygame.display.update()
                                            if challenge == 2:
                                                cave += 1
                                                challenge = 0
                                                frame += 1
                                                user_input = ''
                                                break
                                            else:
                                                challenge += 1
                                                user_input = ''
                                            time.sleep(1)
                                        else:
                                            if lives == 0:
                                                frame = 9
                                                break
                                            else:
                                                lives -= 1
                                                user_text = main_font.render(random.choice(wrong_list), 1, (255, 255, 255))
                                                window.blit(user_text, (300, 450))
                                                pygame.display.update()
                                                time.sleep(4)
                                                user_input = ''
                                window.blit(frame_5, (0, 0))
                                lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                                user_text = main_font.render(user_input, 1, (255, 255, 255))
                                riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                                    (255, 255, 255))
                                press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                                      (255, 255, 255))
                                text_line = main_font.render("______"*8, 1, (255, 255, 255))
                                window.blit(lives_label, (20, 15))
                                window.blit(user_text, (320, 420))
                                window.blit(text_line, (120, 425))
                                window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                                window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                                pygame.display.update()

        if frame == 5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    monster_transition(cave)
                    time.sleep(1)
                    window.blit(frame_6, (0, 0))
                    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                    riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                        (255, 255, 255))
                    press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                          (255, 255, 255))
                    window.blit(lives_label, (20, 15))
                    window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                    window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                    pygame.display.update()
                    if event.key == pygame.K_RETURN and frame == 5:
                        while frame == 5:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_BACKSPACE:
                                        user_input = user_input[:-1]
                                    else:
                                        user_input += event.unicode
                                    if event.key == pygame.K_RETURN:
                                        answer = select_answer(cave, challenge)
                                        user_answer = user_input[:-1]
                                        user_answer = user_answer.lower()
                                        if user_answer == answer:
                                            user_text = main_font.render(random.choice(correct_list), 1,
                                                                         (255, 255, 255))
                                            window.blit(user_text, (300, 450))
                                            pygame.display.update()
                                            if challenge == 2:
                                                cave += 1
                                                challenge = 0
                                                frame += 1
                                                user_input = ''
                                                break
                                            else:
                                                challenge += 1
                                                user_input = ''
                                            time.sleep(1)
                                        else:
                                            if lives == 0:
                                                frame = 9
                                                break
                                            else:
                                                lives -= 1
                                                user_text = main_font.render(random.choice(wrong_list), 1,
                                                                             (255, 255, 255))
                                                window.blit(user_text, (300, 450))
                                                pygame.display.update()
                                                time.sleep(4)
                                                user_input = ''
                                window.blit(frame_6, (0, 0))
                                lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                                user_text = main_font.render(user_input, 1, (255, 255, 255))
                                riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                                    (255, 255, 255))
                                press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                                      (255, 255, 255))
                                text_line = main_font.render("______"*8, 1, (255, 255, 255))
                                window.blit(lives_label, (20, 15))
                                window.blit(user_text, (320, 420))
                                window.blit(text_line, (120, 425))
                                window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                                window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                                pygame.display.update()
        if frame == 6:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    monster_transition(cave)
                    time.sleep(1)
                    window.blit(frame_7, (0, 0))
                    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                    riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                        (255, 255, 255))
                    press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                          (255, 255, 255))
                    window.blit(lives_label, (20, 15))
                    window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                    window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                    pygame.display.update()
                    if event.key == pygame.K_RETURN and frame == 6:
                        while frame == 6:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_BACKSPACE:
                                        user_input = user_input[:-1]
                                    else:
                                        user_input += event.unicode
                                    if event.key == pygame.K_RETURN:
                                        answer = select_answer(cave, challenge)
                                        user_answer = user_input[:-1]
                                        user_answer = user_answer.lower()
                                        if user_answer == answer:
                                            user_text = main_font.render(random.choice(correct_list), 1,
                                                                         (255, 255, 255))
                                            window.blit(user_text, (300, 450))
                                            pygame.display.update()
                                            if challenge == 2:
                                                cave += 1
                                                challenge = 0
                                                frame += 1
                                                user_input = ''
                                                break
                                            else:
                                                challenge += 1
                                                user_input = ''
                                            time.sleep(1)
                                        else:
                                            if lives == 0:
                                                frame = 9
                                                break
                                            else:
                                                lives -= 1
                                                user_text = main_font.render(random.choice(wrong_list), 1,
                                                                             (255, 255, 255))
                                                window.blit(user_text, (300, 450))
                                                pygame.display.update()
                                                time.sleep(4)
                                                user_input = ''
                                window.blit(frame_7, (0, 0))
                                lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                                user_text = main_font.render(user_input, 1, (255, 255, 255))
                                riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                                    (255, 255, 255))
                                press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                                      (255, 255, 255))
                                text_line = main_font.render("______"*8, 1, (255, 255, 255))
                                window.blit(lives_label, (20, 15))
                                window.blit(user_text, (320, 420))
                                window.blit(text_line, (120, 425))
                                window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                                window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                                pygame.display.update()

        if frame == 7:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    monster_transition(cave)
                    time.sleep(1)
                    window.blit(frame_8, (0, 0))
                    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                    riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                        (255, 255, 255))
                    press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                          (255, 255, 255))
                    window.blit(lives_label, (20, 15))
                    window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                    window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                    pygame.display.update()
                    if event.key == pygame.K_RETURN and frame == 7:
                        while frame == 7:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_BACKSPACE:
                                        user_input = user_input[:-1]
                                    else:
                                        user_input += event.unicode
                                    if event.key == pygame.K_RETURN:
                                        answer = select_answer(cave, challenge)
                                        user_answer = user_input[:-1]
                                        user_answer = user_answer.lower()
                                        if user_answer == answer:
                                            user_text = main_font.render(random.choice(correct_list), 1,
                                                                         (255, 255, 255))
                                            window.blit(user_text, (300, 450))
                                            pygame.display.update()
                                            if challenge == 2:
                                                cave += 1
                                                challenge = 0
                                                frame += 1
                                                user_input = ''
                                                break
                                            else:
                                                challenge += 1
                                                user_input = ''
                                            time.sleep(1)
                                        else:
                                            if lives == 0:
                                                frame = 9
                                                break
                                            else:
                                                lives -= 1
                                                user_text = main_font.render(random.choice(wrong_list), 1,
                                                                             (255, 255, 255))
                                                window.blit(user_text, (300, 450))
                                                pygame.display.update()
                                                time.sleep(4)
                                                user_input = ''
                                window.blit(frame_8, (0, 0))
                                lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                                user_text = main_font.render(user_input, 1, (255, 255, 255))
                                riddle_display = riddle_font.render(select_riddle(cave, challenge), 1,
                                                                    (255, 255, 255))
                                press_to_continue = title_font.render("Press ENTER to continue", 1,
                                                                      (255, 255, 255))
                                text_line = main_font.render("______"*8, 1, (255, 255, 255))
                                window.blit(lives_label, (20, 15))
                                window.blit(user_text, (320, 420))
                                window.blit(text_line, (120, 425))
                                window.blit(riddle_display, (width - riddle_display.get_width() - 10, 300))
                                window.blit(press_to_continue, (width - press_to_continue.get_width() - 80, 540))
                                pygame.display.update()

        if frame == 8:
            window.blit(frame_1, (0, 0))
            win = title_font.render("YOU WON THE GAME", 1, (255, 255, 255))
            start_again = main_font.render("Press enter to restart the game", 1, (255, 255, 255))
            game_exit = main_font.render("Press ESC to exit the game", 1, (255, 255, 255))
            window.blit(start_again, (380, 500))
            window.blit(game_exit, (20, 500))
            window.blit(win, (width - win.get_width() - 130, 100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main()
                    if event.key == pygame.K_ESCAPE:
                        run = False
        if frame == 9:
            window.blit(frame_1, (0, 0))
            win = title_font.render("YOU LOST THE GAME", 1, (255, 255, 255))
            start_again = main_font.render("Press enter to restart the game", 1, (255, 255, 255))
            game_exit = main_font.render("Press ESC to exit the game", 1, (255, 255, 255))
            window.blit(start_again, (380, 500))
            window.blit(game_exit, (20, 500))
            window.blit(win, (width - win.get_width() - 130, 100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main()
                    if event.key == pygame.K_ESCAPE:
                        run = False


main()






