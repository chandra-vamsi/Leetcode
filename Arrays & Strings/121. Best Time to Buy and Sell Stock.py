#121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0                         #Initializing a variable to track max_profit
        min_num=float('inf')                 #Initializing a variable to track minimum Number
        for price in prices:                 #Looping(going) through all prices
            if price<min_num:                #checking if the current price is minimum than previous one  
                min_num=price                #if yes change the minimum price to current price
            if price-min_num>max_profit:     #same with max profit will compare price-minimum number
                max_profit=price-min_num
        return max_profit                    #Returning Max_profit



        
