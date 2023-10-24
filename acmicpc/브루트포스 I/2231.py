# 탐색공간 줄이기 대작전

N = 216

Ndgt = 0

def diS(n: int):
    K=n
    dgt = []
    while K:
        K, dg = K//10, K%10
        dgt.append(dg)
    return n+sum(dgt)

K = N
while K:
    K = K // 10; Ndgt += 1
Ndgt = 1 if Ndgt == 1 else Ndgt-1

res = 0
for eta in range(min(N, 9*(Ndgt)),0,-1):
    res = (k := N - eta)
    if diS(k) == N: break
    
print(res)

"""k = N = int(input())
Ndgt = 0
while k:
    k //= 10; Ndgt += 1
print(Ndgt)

res = 0
for dif in range(9*(Ndgt-1), 0, -1):
    gg = gen = N - dif
    gendgt = []
    while gg:
        gg, dgt = gg//10, gg%10
        gendgt.append(dgt)
    if gen + sum(gendgt) == N: res = gen; break
print(res)"""