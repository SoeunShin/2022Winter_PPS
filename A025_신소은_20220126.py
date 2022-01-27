# LeetCode 342 - Power of Four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            while n % 4 == 0:
                n /= 4
            if n == 1:
                return True
            return False