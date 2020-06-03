import pygame, sys, os, time

# Initialize the game
pygame.init()
height = 680
width = 680
window = pygame.display.set_mode((height, width))
pygame.display.set_caption("BO")

# Define clock
clock = pygame.time.Clock()
FPS = 15

# Backgrounds
main_background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),
                                         (width, height))
icon = ""

# Icon

# Eliminar
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 150, 0)
blue = (40, 53, 88)
yellow = (255, 255, 0)
light_green = (0, 100, 0)
light_yellow = (200, 200, 0)
light_red = (150, 0, 0)

# Fonts
title_font = pygame.font.SysFont("comicsans", 60)
main_font = pygame.font.SysFont("comicsans", 30)

# Level 1
level_1 = ["A little girl goes to the store and buys one dozen eggs. As she is going home, all but three break. "
           "How many eggs are left unbroken?...", "If two’s company, and three’s a crowd, what are four and five?...",
           "What is the result of: 2 - 2 x 2 + 2 = ..."]
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
#
# Functions
# Get riddle
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
    riddle = main_font.render(display_challenge, True, (255, 255, 255))
    window.blit(riddle, (20, 200))

# Check answer
def check_answer(cave, challenge):
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

# Display the lives
def display_lives(lives):
    lives_label = title_font.render(f"Lives: {lives}", True, (255, 255, 255))
    window.blit(lives_label, (20, 15))

# Display the level
def display_level(cave):
    level_label = title_font.render(f"Level: {cave}", True, (255, 255, 255))
    window.blit(level_label, (width - level_label.get_width() - 20, 15))

# Display the user characters
def display_user_char(char):
    type_chars = main_font.render(char, True, (255, 255, 255))
    window.blit(type_chars, (50, 400))
    pygame.display.update()

# Display the correct answer
def display_answer(challenge, lives, cave):
    a_exit = False
    if lives == 0:
        give_answer = main_font.render(f"The correct answer is {check_answer(cave, challenge)}")
        pygame.draw.rect(window, (0, 0, 0), (0, 500, 800, 600))
        window.blit(give_answer, (200, 530))
    else:
        give_answer = main_font.render("Correct!!", True, (255, 255, 255))
        pygame.draw.rect(window, (0, 0, 0), (0, 500, 800, 600))
        window.blit(give_answer, (200, 530))

    pygame.display.update()

    while not a_exit:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    a_exit = True
                    break

# Display finished game
def finished_game(lives):
    b_exit = False
    for rectangle in range(0, 600, 20):
        pygame.draw.rect(window, (0, 150, 0), [0, 600-(rectangle), 800, 50+(rectangle)])
        pygame.display.update()
        clock.tick(50)

    clock.tick(1)

    over = main_font.render("YOU FINISHED THE GAME", True, (0, 0, 0))
    final_lives = main_font.render(f"WITH {lives} LIVES", True, (0, 0, 0))
    playAgain = main_font.render("Play Again", True, (0, 0, 0))
    quitGame = main_font.render("Quit", True, (0, 0, 0))

    window.fill((40, 50, 30))
    pygame.display.update()
    clock.tick(5)

    window.blit(over, [100, 200])
    pygame.display.update()
    clock.tick(5)

    window.blit(final_lives, [100, 300])
    pygame.display.update()
    clock.tick(5)

    while not b_exit:                                                                        #Waiting for the answer is user wants to
        window.fill((255, 255, 255))                                                              #play again or quit
        pygame.draw.rect(window, (0, 0, 0), [0,100,800,400])
        pygame.draw.rect(window, (0, 0, 0), [0,0,800,100])
        window.blit(over, (100, 200))
        window.blit(final_lives, (100, 300))

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

# PLAY AGAIN BUTTON
        if 100 + 175 > cur[0] > 100 and 400 + 50 > cur[1] > 400:  # Adding play again or quit button
            pygame.draw.rect(window, light_green, [100, 400, 175, 50])
            if click[0] == 1:
                for printRect in range(0, 610, 10):
                    pygame.draw.rect(window, blue, [0, 600 - (printRect), 800, 50 + (printRect)])
                    pygame.display.update()
                    clock.tick(70)
                gameLoop()
        else:
            pygame.draw.rect(window, green, [100, 400, 175, 50])

# QUIT BUTTON
        if 500 + 100 > cur[0] > 500 and 400 + 50 > cur[1] > 400:
            pygame.draw.rect(window, light_red, [500, 400, 100, 50])
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(window, red, [500, 400, 100, 50])

        window.blit(playAgain, [125, 405])
        window.blit(quitGame, [525, 405])

        pygame.display.update()

        for event_2 in pygame.event.get():
            if event_2.type == pygame.QUIT:
                pygame.quit()
                quit()

# Start Frame

def startScreen():
    clock.tick(1)

    b_Exit = False
    helpLine1 = main_font.render("You need to guess the word that appears on the screen", True, yellow)
    helpLine2 = main_font.render("You will be given 5 chances for each word", True, yellow)
    helpLine3 = main_font.render("There is no time limit", True, yellow)
    helpLine4 = main_font.render("If you think that the word contains certain letter", True, green)
    helpLine5 = main_font.render("Enter that letter and press Enter", True, green)
    helpLine6 = main_font.render("If the word contains it, it would be displayed", True, green)
    helpLine7 = main_font.render("There are 5 levels, and 5 words per level", True, red)
    helpLine8 = main_font.render("Plus 100 points for each correct word multiplied by the level", True, red)
    helpLine9 = main_font.render("plus 10 for each chance left", True, red)
    helpLine0 = main_font.render("100 points deducted if you couldn't guess the word", True, red)

    quitGame = main_font.render("Quit the game", True, red)

    playGame = main_font.render("Play Game!", True, green)

    button1 = main_font.render("Play", True, black)
    button2 = main_font.render("Help", True, black)
    button3 = main_font.render("Quit", True, black)

    Level1Start = title_font.render("Cave 1", True, green)

    window.fill(blue)  # Making BG and displaying the heading
    pygame.display.update()
    clock.tick(1)

    heading = title_font.render("Bo", True, yellow)
    window.blit(heading, [50, 100])
    pygame.display.update()
    clock.tick(1)

    while not b_Exit:
        window.fill(blue)
        window.blit(heading, [50, 100])

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

# PLAY BUTTON
        if 100 + 100 > cur[0] > 100 and 200 + 50 > cur[1] > 200:
            pygame.draw.rect(window, light_green, [100, 200, 100, 50])
            window.blit(playGame, [300, 300])
            if click[0] == 1:
                window.fill(blue)
                window.blit(heading, [50, 100])
                pygame.display.update()
                break
        else:
            pygame.draw.rect(window, green, [100, 200, 100, 50])

        # HELP BUTTON
        if 350 + 100 > cur[0] > 350 and 200 + 50 > cur[1] > 200:
            pygame.draw.rect(window, light_yellow, [350, 200, 100, 50])

            window.blit(helpLine1, [50, 300])
            window.blit(helpLine2, [50, 325])
            window.blit(helpLine3, [50, 350])
            window.blit(helpLine4, [50, 375])
            window.blit(helpLine5, [50, 400])
            window.blit(helpLine6, [50, 425])
            window.blit(helpLine7, [50, 450])
            window.blit(helpLine8, [50, 475])
            window.blit(helpLine9, [50, 500])
            window.blit(helpLine0, [50, 525])

        else:
            pygame.draw.rect(window, yellow, [350, 200, 100, 50])

# QUIT BUTTON
        if 600 + 100 > cur[0] > 600 and 200 + 100 > cur[1] > 200:
            pygame.draw.rect(window, light_red, [600, 200, 100, 50])
            window.blit(quitGame, [300, 300])
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(window, red, [600, 200, 100, 50])

        # DISPLAYING THE WORDS ON BUTTONS
        window.blit(button1, [125, 205])
        window.blit(button2, [375, 205])
        window.blit(button3, [625, 205])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# ANIMATION
    for printRect in range(0, 610, 10):
        pygame.draw.rect(window, yellow, [0, 600 - (printRect), 800, 50 + (printRect)])
        pygame.display.update()
        clock.tick(50)

    window.blit(Level1Start, [300, 250])
    pygame.display.update()
    clock.tick(1)

    for printRect in range(0, 610, 10):
        window.blit(Level1Start, [300, 250])
        pygame.draw.rect(window, blue, [0, 600 - (printRect), 800, 50 + (printRect)])
        pygame.display.update()
        clock.tick(70)

#Function to perform animation at the time of level upgrade
def levelTransition(cave):
    for printRect in range(0,610,10):
        pygame.draw.rect(window, yellow, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)

    textLevelStart = title_font.render("Cave "+str(cave), True, green)             #This displayes level's name
    window.blit(textLevelStart, [300,250])                                         #Loop above and below for animation
    pygame.display.update()
    clock.tick(1)

    for printRect in range(0,610,10):
        window.blit(textLevelStart, [300,250])
        pygame.draw.rect(window, blue, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(70)


# The main game loop
def gameLoop():
    startScreen()
    game_exit = False
    guess_answer = True
    string = ''
    lives = 8
    cave = 1
    challenge = 0
    answer = 0

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if len(string) < 12:
                    char = (chr(event.key))
                    string += char

                if event.type == pygame.K_RETURN:
                    if len(string) == 2:
                        continue
                    string = ''
                    lives -= 1

                    if lives == 0:
                        display_answer(challenge, lives, cave)
                        string = ''
                        lives = 8

                    if event.key == pygame.K_BACKSPACE:
                        string = string[-1]

        if guess_answer == True:
            riddle = select_riddle(cave, challenge)
            answer = check_answer(cave, challenge)
            return riddle, answer

        if answer == string:
            display_user_char(string)
            pygame.display.update()
            challenge += 1




gameLoop()















