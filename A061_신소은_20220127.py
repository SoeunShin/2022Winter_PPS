# LeetCode 168 - Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            remain = (columnNumber-1) % 26
            result += chr(remain + ord('A'))
            columnNumber = (columnNumber-1)//26
        return result[::-1]