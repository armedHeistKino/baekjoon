from math import floor, log2

N, B = map(int, input().split(' '))

tab = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

hdgt = floor(log2(N)/log2(B))
coef = ['0'] * (hdgt+1)

while N:
    dgt = floor(log2(N)/log2(B))
    new_coef, new_N = divmod(N, B**dgt)

    coef[dgt] = tab[new_coef]
    N = new_N

print(''.join(coef[::-1]))