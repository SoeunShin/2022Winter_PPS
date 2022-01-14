# 백준 5598 - 카이사르 암호

word = input()
result = ''

for ch in word:
    if ch in 'ABC':
        result += chr(ord(ch)+23)
    else:
        result += chr(ord(ch)-3)
print(result)