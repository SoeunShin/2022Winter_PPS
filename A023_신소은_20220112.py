# LeetCode - Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        num_list = list(map(int, str(num)))
        num_sum = sum(num_list)
        while num_sum >= 10:
            num_list = list(map(int, str(num_sum)))
            num_sum = sum(num_list)

        return num_sum