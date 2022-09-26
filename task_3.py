a = int(input())
b = int(input())
c = int(input())
n = a + b + c
if a < b < c:
    n = n / 3
    print(n)
elif c < b < a:
    n = n / 2
    print(n)
else:
    print(n)