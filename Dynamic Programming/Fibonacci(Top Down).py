class Solution:
    def fib(self, n: int) -> int:
        memo={0:0,1:1}              #We Define Base cases here
        def f(x):                   #Defining a function to recursively add elements into our memo
            if x in memo:           #Check for the element in memo Hashset(This eliminates the recurrsive calculation)
                return memo[x]      #if found Return
            else:
                memo[x]=f(x-1)+f(x-2) #if not,now will add the branches(Top to down) 
                return memo[x]      
        return f(n)               #calling Function
