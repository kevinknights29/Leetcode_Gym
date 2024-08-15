class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        # Check for both arrays
        size = len(A) + len(B)
        half = size // 2
        if size == 0:
            return 0

        LA = 0
        RA = len(A) - 1

        while True:
            midA = (LA + RA) // 2
            indexB = half - midA - 2

            leftA = A[midA] if midA >= 0 else float("-infinity")
            rightA = A[midA + 1] if (midA + 1) < len(A) else float("infinity")
            leftB = B[indexB] if indexB >= 0 else float("-infinity")
            rightB = B[indexB + 1] if (indexB + 1) < len(B) else float("infinity")

            if (leftA <= rightB) and (leftB <= rightA):
                if size % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                RA = midA - 1
            else:
                LA = midA + 1


# Median:
# if len(merged_array) is odd, then median = merged_array[(n//2) + 1]
# else median = (merged_array[n//2] + merged_array[(n//2) - 1]) / 2

if __name__ == "__main__":
    # Test Cases
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5

    print("All passed!")
