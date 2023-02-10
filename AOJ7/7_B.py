while True:
    
    n, x = map(int, input().split())
    ans = 0
    
    if n == x == 0: break
    
    for h in range (1, n+1):
        for i in range (h+1, n+1):
            for j in range (i+1, n+1):
                if h + i + j == x:
                    ans += 1
                    
    print (ans)
                