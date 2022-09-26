p = int(input())
v = p % 10 + p % 100 // 10 + p % 1000 // 100 + p % 10000 // 1000
if p % 2 == 0:
    if v % 3 == 0:
        print('Норм')
else:
    print("Ujdyj")