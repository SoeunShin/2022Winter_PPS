# LeetCode 204 - Count Primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [1] * n
        prime[0] = 0
        prime[1] = 0
        
        for i in range(2, n):
            if prime[i]:
                prime[2*i:n:i] = [0] * len(prime[2*i:n:i])
        return sum(prime)