class Solution:
    def maxArea(self, height) -> int:
        lptr = 0
        rptr = len(height) - 1
        maxarea = 0
        while lptr <= rptr:
            maxarea = max(maxarea, (rptr - lptr) * min(height[lptr], height[rptr]))
            if height[lptr] <= height[rptr]:
                lptr += 1
            else:
                rptr -= 1
        return maxarea

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

