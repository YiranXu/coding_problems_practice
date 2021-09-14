#Brute Force 
# ---> two for loop, check all possible differences one by one 
#Does not work for super long list
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                if profit>maxprofit:
                    maxprofit=profit
        return maxprofit