class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, j in enumerate(nums):
            rem = target - j
            if rem in nums_dict: return [nums_dict[rem], i]
            nums_dict[j] = i