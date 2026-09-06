class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        def power(x,n):
            ans = 1
            while n >0:
                if n % 2 == 1:
                    ans = (ans * x) % MOD

                x = (x*x) % MOD
                n //= 2
            return ans

        even = (n + 1) // 2
        odd = n // 2
        
        return (power(5, even) * power(4, odd)) % MOD