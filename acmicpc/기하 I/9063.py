N = int(input())

X, Y = [], []
for i in range(N):
    x, y = tuple(map(int, input().split()))
    X.append(x); Y.append(y)

min_x, max_x = min(X), max(X)
min_y, max_y = min(Y), max(Y)

print((max_x - min_x)*(max_y - min_y))