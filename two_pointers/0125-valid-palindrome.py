class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # new_s = ""

        # for c in s:
        #     if (c.isalnum() ): new_s += c

        # new_s = new_s.lower()

        # return new_s == new_s[::-1]

        filtered_s = [c.lower() for c in s if c.isalnum()]
        return filtered_s == filtered_s[::-1]
        