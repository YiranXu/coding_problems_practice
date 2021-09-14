#Two pointers
#refer from https://www.notion.so/121-Best-Time-to-Buy-and-Sell-Stock-6292621d246248d28745907439461408#6ea07bdbe9db46e4ac2f6caca985b148
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,l+1 #left=buy, right=sell
        maxprofit=0
        while(r<=len(prices)-1):
            if prices[r]<=prices[l]:
                l=r #shift the left pointer to the minimum
                r=l+1
            else: #profitable
                profit=prices[r]-prices[l]
                maxprofit=max(maxprofit,profit)
                r=r+1
        return maxprofit