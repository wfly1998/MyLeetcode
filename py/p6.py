class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst = []
        for i in range(min(len(s), numRows)):
            lst.append('')
        row = 0
        direct = 1
        for ch in s:
            lst[row] += ch
            if numRows != 1:
                row += direct
            if row == numRows - 1:
                direct = -1
            elif row == 0:
                direct = 1
        return ''.join(lst)

if __name__ == '__main__':
    sol = Solution()
    print(sol.convert('LEETCODEISHIRING', 3))
    print(sol.convert('LEETCODEISHIRING', 4))

