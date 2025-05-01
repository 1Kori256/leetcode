class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            if c == ")":
                if stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            if c == "]":
                if stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
            if c == "}":
                if stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
        if len(stack) != 0:
            return False
        return True