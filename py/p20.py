class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in bracket:
                if not stack:
                    return False
                if bracket[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
        return not stack
