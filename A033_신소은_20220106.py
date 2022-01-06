max = 0
for i in range(5):
    numList = list(map(int, input().split()))
    sumList = sum(numList)
    if(sumList > max):
        max = sumList
        idx = i+1

print(idx, max)