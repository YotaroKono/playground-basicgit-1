class Dice:
    def __init__(self, saikoro):
        self.dice = saikoro

    def e(self):
        self.dice[0], self.dice[2], self.dice[5], self.dice[3] = self.dice[3], self.dice[0], self.dice[2], self.dice[5]

    def w(self):
        self.dice[0], self.dice[2], self.dice[5], self.dice[3] = self.dice[2], self.dice[5], self.dice[3], self.dice[0]
        
    def n(self):  
        self.dice[0], self.dice[1], self.dice[5], self.dice[4] = self.dice[1], self.dice[5], self.dice[4], self.dice[0]

    def s(self):
        self.dice[0], self.dice[1], self.dice[5], self.dice[4] = self.dice[4], self.dice[0], self.dice[1], self.dice[5]

    def top(self):
        return self.dice[0]


A = Dice(input().split())
x = input()
for X in x:
    if X == "E":
        A.e()
    elif X == "W":
        A.w()
    elif X == "N":
        A.n()
    elif X == "S":
        A.s()
print(A.top())