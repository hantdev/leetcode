class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = {}

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        res = [item[0] for item in sorted_items[:k]]

        return res


        