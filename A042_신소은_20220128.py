# LeetCode 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for i in s:
            if i != '#':
                s_list.append(i)
            else:
                if len(s_list)>0: s_list.pop()

        for i in t:
            if i != '#':
                t_list.append(i)
            else:
                if len(t_list)>0: t_list.pop()

        if ''.join(s_list) == ''.join(t_list):
            return True
        else: return False