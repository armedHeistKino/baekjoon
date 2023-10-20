N, B = map(str, input().split(' '))
B = int(B)

tab = {gly: i for i, gly in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') }

base_digit = len(N)
res = 0
for dgt, n_ in enumerate(N):
    digit = base_digit -dgt -1
    
    res += tab[n_] * B**digit

print(res)