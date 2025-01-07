class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, j in enumerate(nums):

            #nums_dict[i] =j
            rem = target - j
            if rem in nums_dict: return [nums_dict[rem], i]
            nums_dict[j] = i
            

        #for o in range(len(nums_dict)) :
        #    for p in range(o + 1, len(nums_dict)):
        #        nums_sum = nums_dict [o] + nums_dict [p]
        #        if nums_sum==target:
        #            result=[o, p]
        #return result