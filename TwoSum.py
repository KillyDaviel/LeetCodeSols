class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}  # Dictionary to store elements and their indices

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        return []  


 