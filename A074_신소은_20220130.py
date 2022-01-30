# LeetCode 125. Valid Palindrome

"""
Convert all uppercase letters into lowercase letters and removing all non-alphanumeric characters.
Check if it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum, s.lower()))
        if new_s == new_s[::-1]:
            return True
        return False