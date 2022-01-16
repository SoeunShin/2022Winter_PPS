# LeetCode 169 - Majority Element
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = list(set(nums)) # 중복 제거 
        for n in unique:
            if nums.count(n) > len(nums)/2:
                return n 
