class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return res        
        
        # In n(0)
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i+1] > nums[i]:
        #         i += 1
        #     else:
        #         return nums[i+1]
        # return nums[0]
