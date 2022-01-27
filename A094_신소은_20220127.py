# 백준 2941 - 크로아티아 알파벳

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for a in alpha:
    word = word.replace(a, '#')

print(len(word))