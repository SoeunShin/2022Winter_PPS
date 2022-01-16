# 백준 2693 - N번째 큰 수

case = int(input())
for i in range(case):
    nums = sorted(list(map(int, input().split())), reverse=True)
    print(nums[2])