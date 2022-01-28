# LeetCode 412. Fizz Buzz

"""
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                result.append('FizzBuzz')
            elif i%3 == 0:
                result.append('Fizz')
            elif i%5 == 0:
                result.append('Buzz') 
            else:
                result.append(str(i))
        return result