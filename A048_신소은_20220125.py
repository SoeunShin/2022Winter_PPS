# 백준 1316 - 그룹 단어 체커

n = int(input())
group = 0
for i in range(n): # n번 반복
    word = input()
    for j in range(len(word)):
        if j != len(word)-1: # word의 마지막 문자가 아니라면 
            if word[j] == word[j+1]: # 다음 문자가 자신과 같은 문자이면 
                pass
            elif word[j] in word[j+1:]: # 뒤에 자신과 같은 문자가 있으면 
                break # 그룹 단어가 아님 
        else: group += 1
print(group)