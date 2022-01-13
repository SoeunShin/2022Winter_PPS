# 백준 5355 - 화성 수학

num = int(input())
for i in range(num):
    expr = list(map(str, input().split()))
    answer = float(expr[0])
    for j in expr:
        if j == '@': answer *= 3.0
        elif j == '%': answer += 5.0
        elif j == '#': answer -= 7.0
    print("%.2f"%answer)