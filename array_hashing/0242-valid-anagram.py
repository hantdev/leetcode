class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Beats 36.62%
        # return sorted(s) == sorted(t)

        # Beat 6.69%
        # if len(s) != len(t):
        #     return False

        # counts = {}

        # for c1,c2 in zip(s,t):
        #     if c1 in counts.keys():
        #         counts[c1] += 1
        #     else:
        #         counts[c1] = 1
        #     if c2 in counts.keys():
        #         counts[c2] -= 1
        #     else:
        #         counts[c2] = -1

        # for count in counts.values():
        #     if count != 0:
        #         return False
        # return True

        # Beats 83.24%
        list1 = list(s)
        list2 = list(t)

        counts = {}

        for char in list1:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1

        for char in list2:
            if char not in counts:
                counts[char] = -1
            counts[char] -= 1

        for count in counts.values():
            if count != 0:
                return False
        return True
