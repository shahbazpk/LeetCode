class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        result = []
        
        min_diff = float("inf")
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i+1]]]
        

            elif diff == min_diff:
                result.append([arr[i], arr[i+1]])

        return result