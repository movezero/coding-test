list_X = []

n, x = input().split()
n = int(n)
x = int(x)

A = list(map(int, input().split()))

for i in range(n):
    if A[i] < x:
        list_X.append(A[i])

for i in range(len(list_X)):
    print(list_X[i], end=' ')
