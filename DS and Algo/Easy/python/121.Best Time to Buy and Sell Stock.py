class Solution:
    def maxProfit(self, prices:list) -> int:

        if (len(prices) == 0):
            return 0

        minElement = prices[0]
        maxProfit = 0

        for i in prices[1:]:

            if i < minElement:
                minElement = i

            if i - minElement > maxProfit:
                maxProfit = i - minElement

        return maxProfit





sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))