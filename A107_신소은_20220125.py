# 백준 3059 - 등장하지 않는 문자의 합

n = int(input())

for i in range(n): # n번 반복
    sum = 0
    string = input()
    for alph in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if alph not in string:
            sum += ord(alph)
    print(sum)