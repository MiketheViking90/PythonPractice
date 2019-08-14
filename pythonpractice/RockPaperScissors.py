import enum

def playGame(n):
    w1 = 0
    w2 = 0
    endGame = False
    while (not endGame and w1 < n and w2 < n):
        in1 = input("p1? ")
        if (in1 == "quit"):
            return
        in2 = input("p2? ")
        if (in2 == "quit"):
            return

        in1 = Hand(in1)
        in2 = Hand(in2)
        print(playRound(in1, in2))

    if (w1 == w2):
        print ("Tie")
    elif (w1 > w2):
        print ("P1 Wins!")
    else:
        print ("P2 Wins!")

def playRound(in1, in2):
    comp = getWinner(in1, in2)
    if (comp == 0):
        return in1.getName() + " tie!"
    elif (comp == 1):
        return in1.getName() + " p1 winner!"
    else:
        return in2.getName() + " p2 winner!"

def getWinner(in1, in2):
    return in1.compareTo(in2)

class Hand(enum.Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    def getName(self):
        return self.name

    def compareTo(self, otherHand):
        if self is otherHand:
            return 0
        if self is Hand.rock:
            if otherHand is Hand.scissors:
                return 1
            else:
                return -1
        elif self is Hand.paper:
            if otherHand is Hand.rock:
                return 1
            elif otherHand is Hand.scissors:
                return -1
        else:
            if otherHand is Hand.paper:
                return 1
            elif otherHand is Hand.rock:
                return -1

playGame(1)