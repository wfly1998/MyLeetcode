class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = abs(x)
        s = str(a)
        res = int(s[::-1])
        if x < 0:
            res = -res
        if not (-2**31 <= res <= 2**31-1):
            return 0
        return res
