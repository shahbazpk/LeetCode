class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_used: int, close_used: int):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_used < n:
                backtrack(current + "(", open_used + 1, close_used)

            if close_used < open_used:
                backtrack(current + ")", open_used, close_used + 1)
        
        backtrack("", 0, 0)
        return result