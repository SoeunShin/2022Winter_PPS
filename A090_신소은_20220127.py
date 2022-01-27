# LeetCode 26 - Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for n in nums:
            while nums.count(n) > 1:
                nums.remove(n)