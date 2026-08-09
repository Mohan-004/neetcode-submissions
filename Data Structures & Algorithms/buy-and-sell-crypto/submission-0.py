class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        right = 1
        profit = 0
        while right < n :
            if prices[left] < prices[right] :
                profit = max(profit, prices[right]-prices[left])
            else :
                left = right 
            right += 1 

        return profit
