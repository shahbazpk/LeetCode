class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalAbsSum = 0
        smallestAbsValue = float("inf")
        hasOddNagativ = False

        for row in matrix:
            for value in row:
                smallestAbsValue = min(smallestAbsValue, abs(value))

                if value <0:
                    totalAbsSum -= value
                    hasOddNagativ = not hasOddNagativ
                else:
                    totalAbsSum += value

        return totalAbsSum -2 * hasOddNagativ * smallestAbsValue