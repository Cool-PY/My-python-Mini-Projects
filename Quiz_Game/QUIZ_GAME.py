Score = 0

Questions = {1 : "What is the full form of CPU ?",
           2 : "What is the full form of GPU ?",
           3 : "What is the full form of MBR ?",
           4 : "What is the full form of GPT ?",
           5 : "What is the full form of IIT ?"}

while True:
    RULE = """
    You have a score of 0 you have to answer the questions to increase your points.
    If you hit the hiscore of 4 your score will be stored in a hiscore.txt file.

    Good luck!
    """
    print(RULE)
    StartGame = input('Please Enter to continue: ')

    
    QuesDic = {1 : "What is the full form of CPU ?",
            2 : "What is the full form of GPU ?",
            3 : "What is the full form of MBR ?",
            4 : "What is the full form of GPT ?",
            5 : "What is the full form of IIT ?"}

    print(f"Q.1) {QuesDic[1]}")

    Ans1 = input("Enter you answer here: ")
    Ans1 = Ans1.lower()

    if Ans1 == 'central processing unit':
        print("Your answer is correct!")
        Score += 1
        print("Your score is increased by 1")

    else :
        print("Your answer is wrong!")

    print(f"Q.2) {QuesDic[2]}")

    Ans2 = input("Enter your answer here: ")
    Ans2 = Ans2.lower()

    if Ans2 == 'graphic processing unit' or Ans2 == 'graphics processing unit':
        print("Your answer is correct!")
        Score += 1
        print("Your score is increased by 1")

    else :
        print("Your answer is wrong!")

    print(f"Q.3) {QuesDic[3]}")

    Ans3 = input("Enter your answer here: ")
    Ans3 = Ans3.lower()

    if Ans3 == 'master boot record':
        print("Your answer is correct!")
        Score += 1
        print("Your score is increased by 1")

    else:
        print("Your answer is wrong!")

    print(f"Q.4) {QuesDic[4]}")

    Ans4 = input("Enter your answer here: ")
    Ans4 = Ans4.lower()

    if Ans4 == 'guid partition table':
        print("Your answer is correct!")
        Score += 1
        print("Your score is increased by 1")

    else:
        print("Your answer is wrong!")

    print(f"Q.5) {QuesDic[5]}")

    Ans5 = input("Enter your answer here: ")
    Ans5 = Ans5.lower()

    if Ans5 == 'indian institute of technology':
        print("Your answer is correct!")
        Score += 1
        print("Your score is increased by 1")

    else:
        print("Your answer is wrong")

    print('Thanks for playing my game!\nGame Made BY - Divyanshu Pawar\nPlease see my other projects too this is my github: https://github.com/FrozenClue\n')

    StartGameAgain = input("If you want to start the game again, Type yes or no: ")
    StartGameAgain = StartGameAgain.lower()

    if 'y' in StartGameAgain:
        continue

    else:
        break

