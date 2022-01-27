# 백준 2775 - 부녀회장이 될테야

n = int(input())

for _ in range(n):
    k = int(input()) # 층
    n = int(input()) # 호
    fl_0 = [x for x in range(1, n+1)] # 0층 리스트 
    for _ in range(k): # 층 수만큼 반복 
        for j in range(1, n):
            fl_0[j] += fl_0[j-1]
    print(fl_0[-1]) # 마지막 element 출력