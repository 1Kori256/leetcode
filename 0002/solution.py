# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def to_num(self, ll):
        x = ll.val
        power = 10
        while ll.next:
            ll = ll.next
            x = x + ll.val * power
            power *= 10
        return x

    def to_ll(self, n):
        if n < 10:
            return ListNode(n)
        return ListNode(n % 10, self.to_ll(n // 10))

    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        return self.to_ll(self.to_num(l1) + self.to_num(l2))