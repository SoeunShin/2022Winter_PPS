# LeetCode 13 - Roman to Integer

dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i in range(len(s)-1):
        num = dic[s[i]]
        next = dic[s[i+1]]
        if num >= next:
            result += num
        else:
            result -= num
    result += dic[s[len(s)-1]]
    return result