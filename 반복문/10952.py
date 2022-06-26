sumList = []

while(True):
    ab_List = list(map(int, input().split()))
    sum = ab_List[0] + ab_List[1]
    sumList.append(sum)

    if sum == 0:
        for i in range(len(sumList) - 1):
            print(sumList[i])
        break
