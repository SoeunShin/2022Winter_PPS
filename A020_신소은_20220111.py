# 백준 2455 - 지능형 기차

passenger = 0
max = 0

for i in range(4):
    off, on = map(int, input().split())
    passenger -= off
    passenger += on
    if(passenger > max): max = passenger

print(max)