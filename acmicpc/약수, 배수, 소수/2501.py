N, k = map(int, input().split(' '))
fctrs = sorted(list(set([0] + [(N//i if not N%i else 0) for i in range(1,N+1)])))
print(fctrs[k] if k < len(fctrs) else 0)