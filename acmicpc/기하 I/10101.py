a = int(input())
b = int(input())
c = int(input())

if a+b+c != 180: print('Error')
elif a != b and b != c and a != c: print('Scalene')
elif a != 60 or b != 60 or c != 60: print('Isosceles')
else: print('Equilateral')
