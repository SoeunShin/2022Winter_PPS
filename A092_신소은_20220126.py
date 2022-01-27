# LeetCode 922 - Sort Array By Parity II

"""
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
"""
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1 
        for i in range(0, len(nums), 2):
            if nums[i]%2: 
                while nums[j]%2:
                    j+=2
                nums[i],nums[j] = nums[j],nums[i]
        return nums