remList = []
unique = []
cnt = 0
for i in range(10):
    num = int(input())
    rem = num % 42
    remList.append(rem)

for r in remList:
    if r not in unique: unique.append(r)

print(len(unique))