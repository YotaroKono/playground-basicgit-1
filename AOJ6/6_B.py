cards = []
pattern = ["S", "H", "C", "D"]
n = int(input())
for i in range (n):
    x, y = input().split()
    y = int(y)
    if x == "S":
        cards.append(0+y)
    elif x == "H":
        cards.append(13+y)
    elif x == "C":
        cards.append(26+y)
    elif x == "D":
        cards.append(39+y)
        
for k in range (1, 53):
    if not ( k in cards):
        print(pattern[(k-1)//13], (k-1)%13+1)
        