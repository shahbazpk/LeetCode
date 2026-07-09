class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        C=[i:=0]+[i:=i+(prev+maxDiff<x) for prev, x in pairwise(nums)]
        return [C[x]==C[y]for x, y in queries]