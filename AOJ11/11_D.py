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

    def same(self, faces):
        if self.dice[0] == faces[0] and self.dice[1] == faces[1] and self.dice[2] == faces[2] and self.dice[3] == faces[3] and self.dice[4] == faces[4] and  self.dice[5] == faces[5]:
            return True
    
    def hantei(self, faces):
        for _ in range(3):
            for _ in range(3):
                for _ in range(3):
                    for _ in range(3):
                        if self.same(faces):
                            return True
                        self.e()
                    self.s()
                self.w()
            self.n()
        return False



n = int(input())

for i in range(n):
    saikoro_list[i] = list(map(int,input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        dice = Dice(saikoro_list[i])
        if dice.is_same_dice(saikoro_list[j]):
            print('No')
            break
    else:
        continue
    break
else:
    print('Yes')
    