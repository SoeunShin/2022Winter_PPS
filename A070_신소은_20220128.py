# 백준 2164 - 카드2

"""
다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
"""

import sys 
from collections import deque 

N = int(sys.stdin.readline()) 
queue = deque() 

for i in range(N): 
    queue.append(i + 1)

while len(queue) > 1: 
    queue.popleft() 
    queue.append(queue.popleft()) 

print(queue.pop()) 
