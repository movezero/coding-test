T = int(input())
list_A = []
list_B = []
list_Sum = []

for i in range(T):
    a, b = input().split()

    list_A.append(int(a))
    list_B.append(int(b))
    list_Sum.append(int(a) + int(b))

for i in range(T):
    num = i + 1
    print("Case #%d:" % num, list_A[i], "+", list_B[i], "=", list_Sum[i])
