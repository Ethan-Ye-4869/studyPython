# python3.10
from typing import List

class ArrSolution:
    '''
    Q：找到两个数组的中位数-中间位置的数字
    收获：
        1.list[float]是不合法的
        2./运算的结果是float
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r = nums1 + nums2
        r.sort()
        print(str(r))
        __len = len(r)

        if __len % 2 == 0:
            p = int(__len / 2)
            return (r[p] + r[p - 1]) / 2
        else:
            return float(r[int(__len / 2)])

# e = ArrSolution()
# print(str(e.findMedianSortedArrays([1, 3], [2, 4])))