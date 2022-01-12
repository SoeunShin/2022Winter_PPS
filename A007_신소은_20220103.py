num = input().split()
if(sorted(num) == num): print("ascending")
elif(sorted(num)[::-1] == num): print("descending")
else: print("mixed") 
