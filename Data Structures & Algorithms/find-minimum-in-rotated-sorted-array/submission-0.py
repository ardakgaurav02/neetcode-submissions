class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = 1000000

        for i in nums:
            mini  = min(i, mini)

        return mini