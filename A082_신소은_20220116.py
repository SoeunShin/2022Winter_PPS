# 백준 10814 - 나이순 정렬

case = int(input())
arr = []

for i in range(case):
    age, name = input().split()
    arr.append([int(age), name])
arr.sort(key = lambda x : x[0])

for i in arr:
    print(i[0],i[1]) 
