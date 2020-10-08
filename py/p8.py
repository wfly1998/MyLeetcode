class Solution:
    def myAtoi(self, str: str) -> int:
        flag = None
        num = None
        for ch in str:
            if flag is None and num is None and ch == ' ':
                pass
            elif flag is None and num is None and (ch == '+' or ch == '-'):
                if ch == '-':
                    flag = -1
                else:
                    flag = 1
            elif num is None and ch.isdigit():
                num = int(ch)
            elif ch.isdigit():
                num = num * 10 + int(ch)
            else:
                break
        if flag is None:
            flag = 1
        if num is None:
            num = 0
        result = flag * num
        if result >= 2**31 - 1:
            result = 2**31 - 1
        elif result <= -2**31:
            result = -2**31
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi('42'))
    print(sol.myAtoi('   -42'))
    print(sol.myAtoi('4193 with words'))
    print(sol.myAtoi('words and 987'))
    print(sol.myAtoi('-91283472332'))
