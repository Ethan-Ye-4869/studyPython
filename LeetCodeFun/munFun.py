#! python3.10

from typing import List

class EthanNum:
    '''
    # 给定一个整数数组和一个整数目标值，在数组中找出和为目标值的整数，返回其在数组中的位置
    # nums: 整数数组
    # target: 整数目标值
    # 例：nums = [2, 7, 11, 15]，target = 9， return [0, 1]
    '''
    def twoSum(self, nums: List[int] = [2, 7, 11, 15], target: int = 9) -> List[int]:
        '''
        # todo：
            1.暴力解法：从第一个数据开始往后遍历寻找和为target的值
        '''
        # 状态值doing对应todo list
        doing = 1

        if doing == 1:
            __len = len(nums)
            if __len > 1:
                for i in range(0, __len):
                    for j in range(i, __len):
                        if nums[i] + nums[j] == target:
                            return [i, j]

        return [-1, -1]



    '''
    # 罗马数字解析
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    # 规则：VIII - 8；IX - 9
    # 例：MCMXCIV - 1994
    '''
    def romanToInt(self, s: str = 'MCMXCIV') -> int:
        '''
        # todo:
            1.从右往左遍历，加当前位，如果前一位小于当前位，则减去前一位
        '''
        doing = 1
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if doing == 1:
            index = len(s) - 1
            romanInt = 0
            while index >= 0:
                romanInt += roman.get(s[index])
                if index > 0 and roman.get(s[index - 1]) < roman.get(s[index]):
                    index -= 1
                    romanInt -= roman.get(s[index])
                index -= 1
            return romanInt

        return 0


    '''
    # 整数反转
    # 限制：在int整数范围内[-2^31, 2^31 -1]
    '''
    '''
    # 整数反转
    # 范围：[-2^31, 2^31 - 1]
    '''

    def reverse(x: int = -1234) -> int:
        '''
        # todo:
            1.把int转换成字符串处理
            2.直接按int处理
        '''
        doing = 1
        if doing == 1:
            s = str(x)
            start = end = ''
            i_start = 0
            __len = len(s)
            i_end = __len - 1

            if s[i_start] == '-':
                start += s[i_start]
                i_start += 1
            while i_start < i_end:
                start += s[i_end]
                end = s[i_start] + end
                i_start += 1
                i_end -= 1

            if i_start == i_end:
                start += s[i_start]

            r = int(start + end)

            if r > 2 ** 31 - 1 or r <= -2 ** 31:
                return 0
            return r

