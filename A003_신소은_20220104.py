class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(str(_) for _ in digits)) + 1
        return list(map(int, str(num))) 
