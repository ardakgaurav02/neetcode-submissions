class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, n in enumerate(numbers):
            diff = target - n

            if diff in my_dict:
                return [my_dict[diff]+1, i+1]

            my_dict[n] = i
        
        return            

