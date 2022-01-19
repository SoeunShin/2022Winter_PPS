# 백준 2010 - 플러그

import sys
input = sys.stdin.readline

n = int(input())
total = 0

for _ in range(n):
    plug = int(input())
    total += plug

print(total-(n-1))