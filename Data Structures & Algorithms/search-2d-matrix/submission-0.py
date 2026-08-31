class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = 0
        for row in matrix:
            for j in row:
                if j == target:
                    return True
                j += 1
        return False