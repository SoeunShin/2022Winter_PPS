# 백준 3062 - 수 뒤집기

n = int(input())

for i in range(n): # n번 반복 
    num = input()
    num_list = list(num)
    num_list.reverse()
    rev = ''.join(num_list)

    sum = str(int(num) + int(rev))
    if sum == sum[::-1]:
        print('YES')
    else: print('NO')