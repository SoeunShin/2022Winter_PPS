# LeetCode 367 - Valid Perfect Score

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num**0.5
        if int(sqrt) == sqrt:
            return True
        return False