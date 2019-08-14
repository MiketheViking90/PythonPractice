import random


def guessing_game():
    n = random.randint(1, 9)
    cnt = 0
    is_exit = False
    while not is_exit:
        cnt += 1
        user_in = input("Guess? ")
        if user_in == "exit":
            break
        if str.isdigit(user_in):
            user_int = int(user_in)
            if user_int == n:
                print("Correct!")
                return
            elif user_int < n:
                print("Higher")
            else:
                print("lower")


guessing_game()
