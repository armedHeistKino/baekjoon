while True:
    a, b = map(int, input().split(' '))

    if not a and not b: break

    if (a % b) and (b % a):
        print('neither')
    elif (a % b == a):
        print('factor')
    elif (b % a == b):
        print('multiple')