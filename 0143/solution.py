# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        l, r = head, head
        while r and r.next:
            x = l
            l = l.next
            r = r.next.next
        x.next = None
        
        prev = None
        while l:
            next = l.next
            l.next = prev
            prev = l
            l = next
        
        current_l = head
        current_r = prev
        while current_r:
            later_l = current_l.next
            current_l.next = current_r
            current_l = current_r
            current_r = later_l