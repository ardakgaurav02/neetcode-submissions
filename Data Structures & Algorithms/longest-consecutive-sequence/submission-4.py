class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_count = 0

        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while (num + length) in numset:
                    length += 1
                max_count = max(max_count, length)
        return max_count


        # if nums == []:
        #     return 0
        # nums.sort()
        # final_count = 1
        # count = 1
        # j = 1
        # for i in range(0, len(nums)-1):
        #     if nums[i]+1 == nums[j]:
        #         count += 1
        #         i = j
        #         final_count = max(final_count, count)
        #     elif nums[i] != nums[j]:
        #         count = 1 
        #     j += 1
        
        # return final_count