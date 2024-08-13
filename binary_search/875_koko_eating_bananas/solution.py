class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        R = max(piles)
        L = 1
        k_min = R
        while L <= R:
            k = (L + R) // 2
            turns = 0
            for pile in piles:
                turns += (pile / k).__ceil__()
            if turns <= h:
                k_min = min(R, k)
                R = k - 1
            else:
                L = k + 1
        return k_min


# Brute Force
# 1. Select the Max value from the piles array as the initial k
# 2. Check if len(piles) < h:
#   2.1 If len(piles) == h return max(piles)
#   2.2 If len(piles) > h return error | Won't happen given h constraints
# 3. Iterate decreasing k (for k in range(start=max(piles), stop=0, step=-1))
#   3.1 Define turns = 0
#   3.2 for each element in pile:
#       3.2.1 Calculate r = pile % k
#       3.2.2 if r < k and r > 0:
#           3.2.2.1 turns += ((pile // k) + 1)
#       3.2.3 else turns += 1
#   3.3 If turns <= h:
#       3.3.1 proceed to the next iteration
#   3.4 else return k+1 (last valid k)
# Space: O(1) | Time: O(max(pile) * pile)

if __name__ == "__main__":
    # Test Cases
    assert Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

    print("All passed!")
