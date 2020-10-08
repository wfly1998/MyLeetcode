class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_of_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                        'C': 100, 'D': 500, 'M': 1000}
        result_int = []
        for ch in s:
            result_int.append(map_of_roman[ch])
        for index in range(1, len(result_int)):
            if result_int[index-1] < result_int[index]:
                result_int[index] -= result_int[index-1]
                result_int[index-1] = 0
        return sum(result_int)

