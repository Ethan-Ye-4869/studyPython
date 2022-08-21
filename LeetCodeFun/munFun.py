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
            1.枚举法：从第一个数据开始往后遍历寻找和为target的值
            2.hash table：建立一个哈希表存储遍历过的数据，可实现一个for循环查找
        '''
        # 状态值doing对应todo list
        doing = 1

        if doing == 1:
            l = len(nums)
            for i in range(l):
                for j in range(i + 1, l):
                    if nums[i] + nums[j] == target:
                        return [i, j]
        elif doing == 2:
            hashTable = dict()
            for i, num in enumerate(nums):
                if target - num in hashTable:
                    return [hashTable[target - num], i]
                hashTable[num] = i

        return []



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
    # 范围：[-2^31, 2^31 - 1]
    '''

    def reverse(self, x: int = -1234) -> int:
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


    '''
    # 两数相加(非负逆序链表)
    # 100 => 0 -> 0 -> 1
    '''
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # todo:
            1.从左到右相加(最低位开始相加)
        '''



