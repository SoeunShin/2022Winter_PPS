# 백준 11656 - 접미사 배열

word = input()
suffixList = []
for i in range(len(word)):
    suffixList.append(word[i:len(word)+1])

for i in sorted(suffixList):
    print(i)