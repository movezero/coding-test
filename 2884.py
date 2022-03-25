a, b = input().split()

a, b = int(a), int(b)

if (b >= 45) :
    b -= 45
    print(a, b)
elif (a == 0) :
    a = 23
    b += 15
    print(a, b)
else :
    a -= 1
    b += 15
    print(a, b)