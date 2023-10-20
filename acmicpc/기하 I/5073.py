while True:
    e = list(map(int, input().split()))
    a,b,c = e[0], e[1], e[2]

    if a == 0 and b == 0 and c == 0: break

    if sum(e) - max(e) <= max(e): print('Invalid')
    elif a != b and b != c and a != c: print('Scalene')
    elif a == b and b == c and a == c: print('Equilateral')
    else: print('Isosceles')
