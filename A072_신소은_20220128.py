# LeetCode 1154 - Day of the Year

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2])

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        answer = sum(days[:month-1]) + day
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month > 2: # 윤년 계산 
            answer += 1
        return answer