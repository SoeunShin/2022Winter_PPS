# 백준 9546 - 3000번 버스

num = int(input())

for _ in range(num):
    num = int(input())
    person = 1
    for _ in range(num-1):
        person = person * 2 + 1
    print(person)