num = int(input())
for i in range(num):
    answer = input()
    score = 0
    cnt = 0
    for j in answer:
        if j == 'O':
            cnt += 1
            score += cnt
        else: cnt = 0
    print(score)