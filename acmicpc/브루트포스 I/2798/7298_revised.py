N, M = 10, 500 # map(int, input().split(' '))
n = sorted(list(map(int, '93 181 245 214 315 36 185 138 216 295'.split(' '))))

lst = 0
ldf = M
for i in range(L:=len(n)):
    for j in range(i+1,L):
        for k in range(j+1,L):
            if (df:=M-(s:=n[i]+n[j]+n[k]))>=ldf: break
            if M>=s:
                ldf = df
                lst = s
print(lst)