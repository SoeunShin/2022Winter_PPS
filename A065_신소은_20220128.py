# 백준 11650. 좌표 정렬하기

num = int(input())
arr = []

for _ in range(num):
    arr.append(list(map(int, input().split())))
arr.sort(key = lambda x: (x[0], x[1]))

for i in range(num):
    print(arr[i][0], arr[i][1])