n, m = map(int, input().split())
a = [list(map(int, input().split())) for x in range(n)]
b = [int(input()) for y in range(m)]

for i in range (n):
    answer = 0
    for j in range (m):
        answer += a[i][j] * b[j]
    print(answer)
