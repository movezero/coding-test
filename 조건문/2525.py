a, b = input().split()
c = input()

a, b = int(a), int(b)
c = int(c)

b += c

if (b >= 60):
    a += b // 60
    if (a >= 24) :
        a -= 24
    b %= 60

print(a, b)