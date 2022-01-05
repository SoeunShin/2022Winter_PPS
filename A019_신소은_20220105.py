A = int(input())
B = int(input())
C = int(input())
mul = list(map(int, str(A * B * C)))
num = [0 for i in range(10)]

for n in mul:
    num[n] += 1

for i in range(10):
    print(num[i])