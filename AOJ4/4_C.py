while True:
  
    list  = input().split()
    a = int(list[0])
    op = list[1]
    b = int(list[2])
    
    if op == '?':
        break
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a//b)
