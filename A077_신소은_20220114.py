# 백준 2822 - 점수 계산

scores = []
idx = []
sum = 0
for i in range(8):
    scores.append(int(input()))
sortedList = sorted(scores, reverse=True)

for i in range(5):
    sum += sortedList[i]
    idx.append(str(scores.index(sortedList[i])+1))
print(sum)
print(" ".join(sorted(idx)))