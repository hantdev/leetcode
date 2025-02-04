class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Beats 51.31%
        # hashset = set()
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False

        # Beats 76.96%
        # new_nums = list(dict.fromkeys(nums))
        # if len(new_nums) == len(nums):
        #     return False
        # return True

        # Beats 96.21%
        return len(nums) > len(set(nums))
