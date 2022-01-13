# 백준 1159 - 농구 경기

num = int(input())
firstList = []
five = ''
for i in range(num):
    name = input()
    firstList.append(name[0])

unique = sorted(list(set(firstList))) # 중복 문자 제거
for ch in unique:
    if firstList.count(ch) >= 5:
        five += ch

if five == '':
    print("PREDAJA")
else: print(five)