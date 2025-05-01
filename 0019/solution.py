# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        k = 0
        x = head
        while x:
            x = x.next
            k += 1
        x = head
        for _ in range(max(k - n - 1, 0)):
            x = x.next
        if x == head and k - n == 0:
            head = x.next
        elif x.next and x.next.next:
            x.next = x.next.next
        else:
            x.next = None

        return head

        
        
