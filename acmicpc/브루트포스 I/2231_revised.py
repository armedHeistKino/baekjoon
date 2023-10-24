k = N = 1 
Ndgt = 0
while k:
    k //= 10; Ndgt += 1

ans = []
for dif in range(min(N, 9*Ndgt), 0, -1):
    # 분해합 구하기
    gg = gen = N - dif
    digits = []
    while gg:
        gg, dgt = gg//10, gg%10
        digits.append(dgt)

    # 실제로 생성자인지 보기
    if gen + sum(digits) == N: ans.append(gen)

# 최솟값만 빼내기
print(min(ans) if ans else 0)