# 백준 17210 - 문문문

n = int(input())
open = int(input())

if n > 5:
    print('Love is open door')
else:
    for _ in range(n-1):
        open = int(not open)
        print(open)