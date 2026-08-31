class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxp = max(maxp, diff)
            else:
                l = r
            r += 1
        return maxp




    #bruct force
        # maxp = 0
        # for i in range(0, len(prices)-1):
        #     j = i+1
        #     while j <= len(prices)-1:
        #         if prices[j] >= prices[i]:
        #             diff = prices[j] - prices[i]
        #             maxp = max(maxp, diff)
        #         j += 1
        
        # return maxp