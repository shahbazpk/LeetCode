class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for k in count:
            if count[k] > 1:
                return k