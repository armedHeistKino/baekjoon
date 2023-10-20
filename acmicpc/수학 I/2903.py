N = int(input())

tab = [0 for _ in range(N+1)]
tab[0] = 2

for n, t in enumerate(tab[1:]):
    n += 1
    tab[n] += 2*tab[n-1]-1
    
print(tab[N]**2)