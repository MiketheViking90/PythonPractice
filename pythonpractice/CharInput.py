import datetime

def exercise_1():
    #name = input("name? ")
    #age = input("age? ")
    name = "jim"
    age = "29"
    age = int(age)
    curYear = datetime.datetime.now().year
    year100 = curYear + (100-age)

    print("Your name is " + name)
    print("Your age is " + str(age))
    print("You turn 100 yo in " + str(year100))

def extra1(n):
    for i in range(0, n):
        exercise_1()

#exercise_1()
extra1(5)