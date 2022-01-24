# 백준 1193 - 분수 찾기

"""
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
"""

n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    m = line - n + 1
    print(n, '/', m, sep='')
else:
    m = line - n + 1
    print(m, '/', n, sep='')