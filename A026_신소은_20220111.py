# programmers - 하샤드 수

def solution(x):
    x_list = list(map(int, str(x)))
    x_sum = sum(x_list)
    if(x % x_sum == 0): return True
    else: return False