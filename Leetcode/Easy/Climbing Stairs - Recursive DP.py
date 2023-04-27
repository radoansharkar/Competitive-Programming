class Solution(object):
    def climbStairs(self, n):
        mem = [-1] * n
        def dp(now):
            #base
            if now == n:
                return 1
            elif now > n:
                return 0
            
            #memoization 
            if mem[now] != -1:
                return mem[now]

            #transition 
            ans = dp(now + 1) + dp(now + 2)

            mem[now] = ans 

            return mem[now]
        return dp(0)
