# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        found = True
        current = head
        while found:
            found = False
            sums = {0: 0}
            i = 0
            new = current
            cs = 0
            while new:
                i += 1
                x = new.val
                cs += x
                if cs in sums:
                    found = True
                    break
                else:
                    sums[cs] = i
                new = new.next
            if found:
                new = current
                j = 0
                while j < sums[cs] - 1:
                    new = new.next
                    j += 1
                while j < i - 1:
                    new.next = new.next.next
                    j += 1
                if sums[cs] == 0:
                    head = head.next
            current = head
        return current