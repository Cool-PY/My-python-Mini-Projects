# Ex-5

# Start from here

def gettime():
    import datetime
    return datetime.datetime.now()

UserChoice1 = int(input("Please tell what you want to do\nType (1) to add data and (2) to retrieve data: "))

if UserChoice1 == 1:
    print("OK, Now type which data you want add (1) for Exercise (2) for Food")
    UserChoice = int(input("Enter: "))
    if UserChoice == 1:
        print("OK, Now please tell for whom you want to add data\n(1) for Carry (2) for Harry (3) for Rohan")
        UserChoiceName = int(input("Enter: "))
        if UserChoiceName == 1:
            NameExercise = input('Enter the name of the exercise: ')
            with open("CarryExercise.txt", "a") as cf:
                cf.write("Time: " + str(gettime()) + " | " + "Exercise: " + NameExercise + "\n")
                print("Saved successfully!")

        elif UserChoiceName == 2:
            NameExercise2 = input("Enter the name of the exercise: ")
            with open("HarryExercise.txt", "a") as hf:
                hf.write("Time: " + str(gettime()) + " | " + "Exercise: " + NameExercise2 + "\n")
                print("Saved successfully!")

        elif UserChoiceName == 3:
            NameExercise3 = input("Enter the name of the exercise: ")
            with open("RohanExercise.txt", "a") as rf:
                rf.write("Time: " + str(gettime()) + " | " + "Exercise: " + NameExercise3 + "\n")

    elif UserChoice == 2:
        print("OK, Now please tell for whom you want to add data\n(1) for Carry (2) for Harry (3) for Rohan")
        UserChoiceName2 = int(input("Enter: "))
        if UserChoiceName2 == 1:
            FoodName = input("Enter the name of the food: ")
            with open("CarryFood.txt", "a") as cf:
                cf.write("Time: " + str(gettime()) + " | " + "Food: "  + FoodName)
                print("Saved successfully!")

        elif UserChoiceName2 == 2:
            FoodName = input("Enter: ")
            with open("HarryFood.txt", "a") as hf:
                hf.write("Time: " + str(gettime()) + " | " + "Food: "  + FoodName)
                print("Saved successfully!")

        elif UserChoiceName2 == 3:
            FoodName = input("Enter: ")
            with open("RohanFood.txt", "a") as rf:
                rf.write("Time: " + str(gettime()) + " | " + "Food: " + FoodName)
                print("Saved successfully!")

elif UserChoice1 == 2:
    print("OK, Now type which data you want to retrieve (1) for Exercise (2) for Food")
    UserChoice = int(input("Enter: "))

    if UserChoice == 1:
        print("OK, Now please tell for whom you want to see the data\n(1) for Carry (2) for Harry (3) for Rohan")
        UserChoiceName = int(input("Enter: "))

        if UserChoiceName == 1:
            print("OK, Here it is")
            with open("CarryExercise.txt") as cf:
                print(cf.read())

        elif UserChoiceName == 2:
            print("OK, Here it is")
            with open("HarryExercise.txt") as hf:
                print(hf.read())

        elif UserChoiceName == 3:
            print("OK, Here it is")
            with open("RohanExercise.txt") as rf:
                print(rf.read())

    elif UserChoice == 2:
        print("OK, Now please tell for whom you want to see the data\n(1) for Carry (2) for Harry (3) for Rohan")
        UserChoiceName = int(input("Enter: "))

        if UserChoiceName == 1:
            print("OK, Here it is")
            with open("CarryFood.txt") as cf:
                print(cf.read())

        elif UserChoiceName == 2:
            print("OK, Here it is")
            with open("HarryFood.txt") as hf:
                print(hf.read())

        elif UserChoiceName == 3:
            print("OK, Here it is")
            with open("RohanFood.txt") as rf:
                print(rf.read())
