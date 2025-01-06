#70. Climbing Stairs.py
#https://leetcode.com/problems/climbing-stairs/description/
#Bottomup approach(Tabulation)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:                  #setting our base cases
            return 1
        if n==2:
            return 2
        dp =[0]*(n)
        dp[0]=1            
        dp[1]=2
        for i in range(2,n):         #looping other than base cases
            dp[i]=dp[i-2]+dp[i-1]    #Setting ith element with the total ways by adding ways that previous two steps can be reached 
        return dp[-1]                #returning last element
#Top Down Approach (Memorization)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo={1:1,2:2}
        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n]=f(n-2)+f(n-1)
                return memo[n]
        return f(n)
