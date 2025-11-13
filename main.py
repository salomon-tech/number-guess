from random import randint

user = input("user name : ")
machine_think = randint(0, 10)
number_trying = 0

while True:
    try:
        user_preposition = int(input("enter your proposition (0-10) : "))
        number_trying +=1
        if machine_think == user_preposition:
            print(f"congratulations {user} you found the number in {number_trying} tries ")
            continue_preposition = input("do u want ro continoue ? (y/n) : ")
            while continue_preposition not in ['y', 'n']:
                continue_preposition = input("please enter a valid choice (y/n) : ")
                if continue_preposition == 'y':
                    machine_think = randint(0, 10)
                    number_trying = 0
            if continue_preposition == 'n':
                print(f"thank u for playing, goodbye {user} !")
                break
        elif machine_think < user_preposition:
            print("the number is higher, please try again!")
        elif machine_think > user_preposition:
            print("the number is lower, please try again !")

    except ValueError:
        print("please enter a valid number to play the game ! ")
    