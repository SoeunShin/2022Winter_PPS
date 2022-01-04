num = int(input())
scores = []

for i in range(num):
    scores.append(list(map(int, input().split())))

for i in range(len(scores)):
    score_sum = 0
    stu_sum = 0

    for j in range(1, scores[i][0]+1):
        score_sum += scores[i][j]
    avg = score_sum / scores[i][0]

    for k in range(1, scores[i][0]+1):
        if(scores[i][k] > avg):
            stu_sum += 1
    result = stu_sum / scores[i][0] * 100
    print("{:.3f}%".format(result))