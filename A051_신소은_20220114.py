# 백준 5622 - 다이얼

alpha = input()
time = 0
a_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for ch in alpha:
    for i in range(len(a_list)):
        if ch in a_list[i]:
            time += i+3
print(time)