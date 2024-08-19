class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        L = 0
        R = 1
        # iterate over prices
        while R < len(prices):
            # check futures prices for a buy and sell opportunity
            if prices[R] > prices[L]:
                # store max profit seen so far
                max_profit = max(max_profit, prices[R] - prices[L])
            else:
                # update the left pointer to right's position
                L = R
            # increase the right pointer
            R += 1
        return max_profit


if __name__ == "__main__":
    # Test Cases
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0

    print("All passed!")
