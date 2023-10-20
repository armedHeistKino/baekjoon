while True:
    N = int(input())
    if N == -1: break

    fctrs = sorted(list(set([0] + [(N//i if not N%i else 0) for i in range(1,N+1)])))[1:-1]
    if N == sum(fctrs):
        print(f'{N} = {" + ".join([str(f) for f in fctrs])}')
    else:
        print(f'{N} is NOT perfect.')