# LeetCode - Self Dividing Numbers

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers = [i for i in range(left, right+1)]
        answer = []

        for num in numbers:
            n_list = list(map(int, str(num)))
            flag = 0
            for i in range(len(n_list)):
                if n_list[i] == 0:
                    flag = 1
                    break
                if num % n_list[i] != 0:
                    flag = 1
                    break

            if flag == 0:
                answer.append(num)

        return answer