class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rptr = 0
        maxlen = 0
        ch = set()
        n = len(s)
        for ptr in range(n):
            if ptr > 0:
                ch.remove(s[ptr-1])
            while rptr < n and s[rptr] not in ch:
                ch.add(s[rptr])
                rptr += 1
                maxlen = max(maxlen, len(ch))
        return maxlen

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcabcbb'))
    print(sol.lengthOfLongestSubstring('bbbbb'))
    print(sol.lengthOfLongestSubstring('pwwkew'))

