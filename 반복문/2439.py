n = int(input())

for i in range(1, n + 1):
    num = n - i
    print(' ' * num, end='')
    print("*" * i)
