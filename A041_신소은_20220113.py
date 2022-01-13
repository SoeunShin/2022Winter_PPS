# programmers - JadenCase 문자열 만들기

def solution(s):
    s_list = s.split(" ")
    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()
    return " ".join(s_list)