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


#e = Solution()
#print(e.isPalindrome(0))