class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        n = len(energyDrinkA)

        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return max(energyDrinkA[0], energyDrinkB[0])

        # Initialize dp arrays
        dpA = [0] * n  # Max energy when ending with drink A
        dpB = [0] * n  # Max energy when ending with drink B

        # Initialize the first element
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]

        # Fill the dp arrays
        for i in range(1, n):
            dpA[i] = max(dpA[i - 1] + energyDrinkA[i], dpB[i - 1])
            dpB[i] = max(dpB[i - 1] + energyDrinkB[i], dpA[i - 1])

        # Return the maximum of the last elements of both arrays
        return max(dpA[-1], dpB[-1])


if __name__ == "__main__":
    # Test Cases
    assert Solution().maxEnergyBoost([1, 3, 1], [3, 1, 1]) == 5
    assert Solution().maxEnergyBoost([4, 1, 1], [1, 1, 3]) == 7

    print("All passed!")
