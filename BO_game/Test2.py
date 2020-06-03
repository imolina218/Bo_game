import pygame, sys, os

width, height = 680, 680
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bo game")

# Load images
frame_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),
                                         (width, height))
frame_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-black_LI.jpg")),
                                         (width, height))
frame_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Inkedbackground-back_L")),
                                         (width, height))

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

# Check answer
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

game = True

while game:
    cave = 1
    challenge = 0
    lives = 8
    run = True
    user_name = ''

    while run:
        riddle = select_riddle(cave, challenge)
        answer = select_answer(cave, challenge)
        print(riddle)
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







