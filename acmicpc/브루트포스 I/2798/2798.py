N, M = 5, 21# map(int, input().split(' '))
nbrs = sorted(list(map(int, '5 6 7 8 9'.split(' '))))

latest = 0
ldiff = M
for i, I in enumerate(nbrs):
    for j, J in enumerate(A:=nbrs[i+1:]):
        for k, K in enumerate(A[j+1:]):
            if M >= (s := I+J+K) and (df := M - s) < ldiff:
                ldiff = df 
                latest = s

print(latest)