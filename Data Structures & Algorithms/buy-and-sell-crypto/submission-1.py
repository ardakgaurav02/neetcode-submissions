class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(0, len(prices)-1):
            j = i+1
            while j <= len(prices)-1:
                if prices[j] >= prices[i]:
                    diff = prices[j] - prices[i]
                    maxp = max(maxp, diff)
                j += 1
        
        return maxp