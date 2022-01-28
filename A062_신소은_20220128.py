# programmers - 2016년

def solution(a, b):
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    all = sum(num[:a-1]) + b
    return day[all % 7] 
