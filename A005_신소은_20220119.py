# programmers - 스킬트리

def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        str = ''
        for i in tree:
            if i in skill:
                str += i
        if str == skill[:len(str)]:
            cnt += 1
            
    return cnt