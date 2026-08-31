class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        final_count = 1
        count = 1
        j = 1
        for i in range(0, len(nums)-1):
            if nums[i]+1 == nums[j]:
                count += 1
                i = j
                final_count = max(final_count, count)
            elif nums[i] != nums[j]:
                count = 1 
                

            j += 1
        
        return final_count

# # [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]

# # count = 4
# max = 4
