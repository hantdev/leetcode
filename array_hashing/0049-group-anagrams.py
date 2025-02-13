class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = defaultdict(list)

        for s in strs: # n
            count = [0] * 26 # a ... z

            for c in s: # m
                # Map a - 0, b - 1, ..., z - 25
                count[ord(c) - ord("a")] += 1
            # immutable -> hashable
            key = tuple(count)
            anagrams_dict[key].append(s)

        # print(anagrams_dict)

        return anagrams_dict.values()

        # Time: O(n * m) Space: O(n * m)
            
        