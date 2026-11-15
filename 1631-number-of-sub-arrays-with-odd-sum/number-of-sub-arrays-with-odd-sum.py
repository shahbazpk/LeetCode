class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = sum(p & 1 for p in accumulate(arr))  # odd prefix sums
        return odd * (len(arr) + 1 - odd) % (10**9 + 7)