N, B = map(int, input().split(' '))

tab = {i: gly for i, gly in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') }

hstd = 0
while B**(hstd+1) <= N: hstd += 1

coeff = ['0'] * (hstd+1)

while N:
    hd = 0
    while B**(hd+1) <= N: hd += 1
    coeff[hd] = tab[cf := int(N / B**hd)]
    N %= cf * B**hd

print(''.join(coeff[::-1]))