class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Beats 18.56%
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # Beats 49.11%
        # for i, x in enumerate(nums): 
        #     c = target - x
        #     if c in nums[i+1:]:
        #         return [i, nums.index(c, i+1)]

        # Beats 68.14%
        dict = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in dict:
                return [dict[c], i]
            dict[num] = i
        