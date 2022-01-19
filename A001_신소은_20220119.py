# LeetCode 455 - Assign Cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        result = 0
        idx = 0
        for cookie in range(0, len(s)):
            for greed in range(idx, len(g)):
                if s[cookie] >= g[greed]:
                    result += 1
                    idx = greed + 1
                    break

        return result