# 백준 14487 - 욱제는 효도쟁이야!!

num = int(input())
cost = list(map(int, input().split(' ')))

print(sum(cost) - max(cost))