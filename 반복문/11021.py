T = int(input())
list = []

for i in range(T):
    a, b = input().split()
    list.append(int(a) + int(b))

for i in range(T):
    num = i + 1
    print("Case #%d:" % num, list[i])
