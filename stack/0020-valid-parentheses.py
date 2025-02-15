class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s) %2 != 0): return False

        stack = []

        for c in s:
            if c in "{[(":
                stack.append(c)
            elif c in "}])":
                if not stack: 
                    return False
                if (c == "}" and stack[-1] == "{") or \
                   (c == "]" and stack[-1] == "[") or \
                   (c == ")" and stack[-1] == "("):
                        stack.pop()
                else:
                    return False

        return len(stack) == 0
        