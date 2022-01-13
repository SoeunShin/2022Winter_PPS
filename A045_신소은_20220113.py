# 백준 1157 - 단어 공부

word = input().upper()
unique = list(set(word)) # 중복 문자 제거
cntList = []

for ch in unique:
    cntList.append(word.count(ch))

if cntList.count(max(cntList)) > 1:
    print('?')
else:
    idx = cntList.index(max(cntList))
    print(unique[idx])