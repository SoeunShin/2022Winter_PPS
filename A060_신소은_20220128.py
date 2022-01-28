# LeetCode 682 - Baseball Game

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for i in ops:
            try: arr.append(int(i))
            except:
                if i == "C": arr.pop()
                elif i == "D": arr.append(arr[-1]*2)
                elif i == "+": arr.append(arr[-1]+arr[-2])
        return sum(arr) 
