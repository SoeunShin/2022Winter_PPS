# 백준 1755 - 숫자놀이

m, n = map(int, input().split())
dic = {'0':'9', '1':'4', '2':'8', '3':'7', '4':'2', '5':'1', '6':'6', '7':'5', '8':'0', '9':'3'}
lst = []

for i in range(m, n+1): 
    itoa = ' '.join([dic[j] for j in str(i)]) 
    lst.append([i, itoa]) 
lst.sort(key=lambda x:x[1]) 

for i in range(len(lst)): 
    if i%10 == 0 and i!= 0: print()
    print(lst[i][0], end=' ')