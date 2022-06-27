# python 3.10

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListSolution:
    '''反向存在链表中的两数相加'''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = index = None
        i1, i2 = l1, l2
        ten = False

        while i1 != None or i2 != None:
            val = 0

            if ten == True:
                val += 1
                ten = False

            if i1 != None:
                val += i1.val
                i1 = i1.next

            if i2 != None:
                val += i2.val
                i2 = i2.next

            if val > 9:
                ten = True
                val -= 10

            if r == None:
                r = index = ListNode(val)
            else:
                index.next = ListNode(val)
                index = index.next

        if ten == True:
            index.next = ListNode(1)

        return r