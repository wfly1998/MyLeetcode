class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return strs[0][:([len(set(ch))==1 for ch in zip(*strs)] + [False]).index(False)] if strs else ''

