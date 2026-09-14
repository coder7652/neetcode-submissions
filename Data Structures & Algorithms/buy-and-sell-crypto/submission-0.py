#https://www.geeksforgeeks.org/dsa/window-sliding-technique/ - refer this for quick revision
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1 #left=buy right=sell
        maxP=0 #max profit
        
        while r < len(prices):   # rightpointer has not passed end of prices
            #profitable
            if prices[l] < prices[r] :
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) # max of cureent maxP and profit we just computed
            else:
                l = r  # dont shift l pointer by 1 , but we need l to be min so shift it directly to r
            r +=1 # shift r by 1
        return maxP
        