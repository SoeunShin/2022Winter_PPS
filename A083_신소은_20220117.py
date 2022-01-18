# 백준 10867 - 중복 빼고 정렬하기

cnt = int(input())
nums = sorted(list(set(map(int, input().split()))))
print(' '.join(str(_) for _ in nums))