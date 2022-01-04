nums = list(map(int, input().split()))
sum = 0
for i in range(len(nums)):
    sum += pow(nums[i], 2)
print(sum % 10)