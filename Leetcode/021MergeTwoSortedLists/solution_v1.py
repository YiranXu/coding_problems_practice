class Solution:
    def maxProfit(self, prices):
        max_p=0
        sorted_prices=sorted(prices)
        smallest=0
        largest=len(prices)-1
        if prices.index(sorted_prices[largest])>prices.index(sorted_prices[smallest]):
            print("jjjj",sorted_prices[largest])
            return sorted_prices[largest]-sorted_prices[smallest]
        else:
            while largest>smallest:
                t1=sorted_prices[largest]-sorted_prices[smallest+1]
                t2=sorted_prices[largest-1]-sorted_prices[smallest]
                if t1>=t2:
                    max_p=t1
                    if prices[::-1].index(sorted_prices[largest])>prices.index(sorted_prices[smallest+1],):
                        return max_p
                elif t1<t2:
                    max_p=t2
                    if prices[::-1].index(sorted_prices[largest-1])>prices.index(sorted_prices[smallest]):
                        return max_p
                
                largest=largest-1
                smallest=smallest+1
            return 0

if __name__ == "__main__":
    a=Solution()
    print("answer",a.maxProfit([2,1,2,0,1]))