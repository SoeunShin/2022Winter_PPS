# programmers - K번째수
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수 구하기

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]
        finish = commands[i][1]
        idx = commands[i][2]
        sortedList = sorted(array[start-1:finish]) 
        answer.append(sortedList[idx-1])
    return answer