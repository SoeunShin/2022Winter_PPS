# programmers - 구명 보트

def solution(people, limit):
    boat = 0
    people.sort()
    start = 0
    end = len(people)-1
    
    while start <= end:
        boat += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return boat