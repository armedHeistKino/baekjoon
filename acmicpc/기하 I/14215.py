e = list(map(int, input().split(' ')))
Se, Me = sum(e), max(e)
print(Se if e[0] == e[1] and e[1] == e[2] else 2*(Se - Me) - 1)