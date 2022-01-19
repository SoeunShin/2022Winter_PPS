# LeetCode 118 - Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):     
            lst = [1] * (i+1)                               # 첫 번째 두 row에 대해 1로 구성된 리스트 생성
            if (i+1) > 2:                                   # 3번째 row 이상이면 
                for j in range(len(result[-1])-1):
                    new = result[-1][j] + result[-1][j+1]   # 이전 row의 합을 계산 
                    lst[0] = 1
                    lst[-1] = 1
                    lst[j+1] = new
            result.append(lst)
        
        return result