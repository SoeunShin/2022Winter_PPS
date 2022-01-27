# 백준 4659 - 비밀번호 발음하기

"""
모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
"""

while True:
    exist = 0
    cnt_vowel = 0 # 모음 개수 cnt
    cnt_cons = 0 # 자음 개수 cnt
    vowel = 0 # 모음 3개 연속 
    cons = 0 # 자음 3개 연속 
    same = 0 # 같은 글자 2번 연속 
    pw = input()
    if pw == 'end': break
    for i in range(len(pw)):
        if pw[i] in 'aeiou': # 모음 
            exist = 1
            cnt_vowel += 1 # 모음 개수 cnt
            cnt_cons = 0
            if cnt_vowel == 3:
                vowel = 1 # 모음 연속 3번 
        else: # 자음
            cnt_cons += 1 # 자음 개수 cnt
            cnt_vowel = 0
            if cnt_cons == 3:
                cons = 1 # 자음 연속 3번 
        if i < len(pw)-1 and pw[i] == pw[i+1] and pw[i] != 'e' and pw[i] != 'o': # 같은 글자 연속 확인 
            same = 1 # 같은 글자 연속 있음 
    if exist == 1 and vowel == 0 and cons == 0 and same == 0:
        print('<', pw, '> is acceptable.', sep='')
    else:
        print('<', pw, '> is not acceptable.', sep='')