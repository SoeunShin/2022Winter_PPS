# 백준 1431. 시리얼 번호

def sumNumber(s):
    res = 0
    for i in s:
        if i.isdigit():
            res += int(i)
    return res

n = int(input())
number = [input().rstrip() for _ in range(n)]
number.sort(key = lambda x: (len(x), sumNumber(x), x))

for i in number:
    print(i)