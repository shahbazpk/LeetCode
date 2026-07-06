class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        a, b, cnt=-1, -1, 0
        for c, d in intervals:
            if c>a and d>b:
                a=c
                cnt+=1
            b=max(b, d)
        return cnt