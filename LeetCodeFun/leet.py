# python 3.10

class Solution:
    '''判断是否为回文数'''
    def isPalindrome(self, x: int) -> bool:
        '''
        # todo
            1.字符串
            2.运算
        '''
        doing = 2

        if doing == 1:
            s = str(x)
            return s == s[::-1]
        elif doing == 2:
            r = False
            if x < 0 or (x != 0 and x % 10 == 0):
                return r
            p = x % 10
            i = x - p
            while i > 0:
                i = i / 10
                p = p * 10 + i % 10
                i -= i % 10
            p = int(p)
            if p == x:
                r = True
            return r

    '''字符串转整数, 0-9 : 48-57'''
    def myAtoi(self, s: str) -> int:
        ''' 清除空格 + 第一个符号正负或数字 + 转换'''
        __len = len(s)

        r = i = 0
        isPositive = True # 正数

        while i < __len:
            if s[i] == ' ':
                i += 1
                continue
            else:
                break

        if i < __len and s[i] == '+':
            i += 1
        elif i < __len and s[i] == '-':
            isPositive = False
            i += 1

        while i < __len:
            bit  = ord(s[i]) - 48
            if bit >= 0 and bit <= 9:
                r = r * 10 + bit
                i += 1
            else:
                break

        if r > 0 and isPositive == False:
            r = -r

        if r < -2 ** 31:
            r = -2 ** 31
        if r > 2 ** 31 -1:
            r = 2 ** 31 -1

        return r


#e = Solution()
#print(e.isPalindrome(0))