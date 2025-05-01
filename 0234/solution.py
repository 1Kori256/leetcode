# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l, r = head, head
        while r and r.next:
            l = l.next
            r = r.next.next

        if r:
            l = l.next
        
        prev = None
        while l:
            next = l.next
            l.next = prev
            prev = l
            l = next
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True