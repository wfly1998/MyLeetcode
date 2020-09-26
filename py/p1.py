class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            n = nums[i]
            if d.get(target-n) is not None:
                return [d[target-n], i]
            else:
                d[n] = i
        print(d)
        
if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))

