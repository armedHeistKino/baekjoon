T = int(input())
C = list(int(input()) for _ in range(T))

coins = [25, 10, 5, 1]
res = [[0, 0, 0, 0] for _ in range(T)]

for icase, case in enumerate(C):
    mtc = case    
    for icn, coin in enumerate(coins): 
        (r := res[icase])[icn], mtc = divmod(mtc, coin)
        
    print(f'{r[0]} {r[1]} {r[2]} {r[3]}')
