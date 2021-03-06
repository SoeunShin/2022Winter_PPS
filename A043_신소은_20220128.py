# LeetCode 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(strs[0])):
            prefix += strs[0][i]
            for j in range(1, len(strs)):
                if strs[j].startswith(prefix):
                    continue
                else:
                    return prefix[:-1]
        return prefix 
