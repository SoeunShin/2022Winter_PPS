# LeetCode 1704 - Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s_list = list(s.lower())
        cnt_l, cnt_r = 0, 0
        for i in range(int(len(s_list)/2)): # 왼쪽 부분 검사 
            if s_list[i] in "aeiou":
                cnt_l += 1
        for i in range(int(len(s_list)/2), len(s_list)): # 오른쪽 부분 검사 
            if s_list[i] in "aeiou":
                cnt_r += 1
        if cnt_l == cnt_r: # 모음 개수가 같으면 
            return True
        else: return False