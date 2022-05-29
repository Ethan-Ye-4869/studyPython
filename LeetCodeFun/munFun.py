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



