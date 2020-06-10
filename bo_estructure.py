def game_start():
    def status():
        print("{0} status is: \n>>{1} lives. \n>>{2} points. "
              "\n>>{3} complete challenges.\n".format(user_name, lives,
                                                      score, level))

    def run_out():
        if lives <= 0:
            confirmation = input("You run out lives, do you want to play again?...").lower()
            if confirmation in "yes":
                game_start()
            else:
                raise SystemExit

    print("Welcome to the Dragon Kingdom game.")
    print(">>You are going have to entmer the different caves and solve puzzles.")
    print(">>You'll get 40 points for each correct puzzle.")
    print(">>There are 3 caves with each 3 mathematical problems and tricky riddles.")
    print(">>You start the game with 4 lives, if you run out of them loose the game and have the option "
          "to restart it.\n")
    game = True
    while game:
        user_name = input("Enter a name for your character: ...")
        lives = 4
        score = 0
        total_score = 360
        level = 0
        print()
        status()
        print()
        raghnak = True
        lordk = True
        usarkna = True
        while raghnak:
            print("Welcome {} to the level of Raghnak".format(user_name))
            print("Let's start with an easy one: a... riddle")
            rag_challenge01 = input("The more of this there is, the less you see. What is it?... ").lower()
            if rag_challenge01 in "darkness":
                print("Well done, maybe i under estimated you, this is going to be fun. NEXT!\n")
                score += 40
                level += 1
            else:
                print("Hmmm.. that doesn't seem right, you know the rules i will take 1 life.\n")
                lives -= 1
            print("Let's put your maths to test.(all the maths problems responses are literal numbers)")
            rag_challenge02 = input("What is the result of: 2 - 2 x 2 + 2 = ...")
            rag_challenge02 = int(rag_challenge02)
            if rag_challenge02 == 0:
                print("Well done, NEXT!\n")
                score += 40
                level += 1
            else:
                print("Hmmm.. that doesn't seem right, you know the rules i will take 1 life.\n")
                lives -= 1
            print("Last one and you go to Lordk.")
            rag_challenge03 = input("If two’s company, and three’s a crowd, what are four and five?...")
            rag_challenge03 = int(rag_challenge03)
            if rag_challenge03 == 9:
                print("Well done. You Are allow to go to the next level.\n")
                score += 40
                level += 1
            else:
                print("Hmmm.. that doesn't seem right, you know the rules i will take 1 life.\n")
                lives -= 1
            raghnak = False
        status()
        while lordk:
            print("Welcome {} to the level of LordK".format(user_name))
            print("Let's heat the game little with a... riddle")
            lord_challenge01 = input("What five-letter word becomes shorter when you add two letters to it?...").lower()
            if lord_challenge01 in "short":
                print("Nice, NEXT ONE!\n")
                score += 40
                level += 1
            else:
                print("WRONG!! you know the rules i will take 1 life.\n")
                lives -= 1
                run_out()

            print("Pay attention, most of the people fail.(all the maths problems responses are literal values)")
            lord_challenge02 = input("In a feast everyone shook hands with everybody else. There were 66 "
                                     "handshakes.\n How many people were at the feast ?...")
            lord_challenge02 = int(lord_challenge02)
            if lord_challenge02 == 12:
                print("Nice you'r big brain, NEXT!\n")
                score += 40
                level += 1
            else:
                print("Hmmm.. that doesn't seem right, you know the rules i will take 1 life.\n")
                lives -= 1
                run_out()

            print("Last one and you go to the final boss.")
            lord_challenge03 = input("A little girl goes to the store and buys one dozen eggs. As she is going "
                                     "home, all but three break. How many eggs are left unbroken?...")
            lord_challenge03 = int(lord_challenge03)
            if lord_challenge03 == 3:
                print("You are more than prepare to go to the next level, or maybe not, who knows right?? JAJAJA.\n")
                score += 40
                level += 1
            else:
                print("Hmmm.. that doesn't seem right, you know the rules i will take 1 life.\n")
                lives -= 1
                run_out()
            lordk = False
        status()
        while usarkna:
            run_out()

            print("Welcome {} to the last level the level of Usarkna".format(user_name))
            print("FOCUS, you'll need it but don't let that play against you, don't enter a brain maze.\n")
            lord_challenge01 = input("What is so fragile that saying its name breaks it?...").lower()
            if lord_challenge01 in "silence":
                print("Hmm, let's go with the next one!\n")
                score += 40
                level += 1
            else:
                print("WRONG!! I will take 1 life.\n")
                lives -= 1
                run_out()

            print("Pay attention.")
            lord_challenge02 = input("I have lakes with no water, mountains with no stone and cities "
                                     "with no buildings. What am I?...")
            lord_challenge02 = lord_challenge02.lower()
            if lord_challenge02 in "map":
                print("Okay you might win, NEXT!\n")
                score += 40
                level += 1
            else:
                print("Hmmm.. that doesn't seem right, I will take 1 life.\n")
                lives -= 1
                run_out()

            print("Last one and you win or loose. Don't rush THINK!!")
            lord_challenge03 = input("What does man love more than life, hate more than death or mortal strife;"
                                     " that which contented men desire; the poor have, the rich require; the miser"
                                     " spends, the spendthrift saves, and all men carry to their graves?...")
            lord_challenge03 = lord_challenge03.lower()
            if lord_challenge03 in "nothing":
                print("WELL DONE !!! you win the game\n")
                score += 40
                level += 1
                print("You won the game with {0} points of {1} and {2} lives".format(score, total_score, lives))

            else:
                print("Hmmm.. that doesn't seem right, I will take 1 life.\n")
                lives -= 1
                run_out()
            usarkna = False
        status()


game_start()














