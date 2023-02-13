while True:
    x = str(input())
    sum = 0
    if x == "0": break
    for i in range(len(x)):
        sum += int(x[i])
    print(sum)
    