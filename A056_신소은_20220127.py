# LeetCode 496 - Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            idx = nums2.index(n)
            flag = 0
            for m in nums2[idx+1:]:
                if n < m:
                    result.append(m)
                    flag = 1
                    break
            if flag == 0: result.append(-1)
        return result